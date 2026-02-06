import json
import random

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from core.data.questions import CODE_QUESTIONS, HR_QUESTIONS, MCQ_QUESTIONS, TECHNICAL_QUESTIONS


def home(request):
    return render(request, "core/home.html")


def login_view(request):
    return render(request, "core/login.html")


def signup_view(request):
    return render(request, "core/signup.html")


def aptitude_view(request):
    return render(request, "core/aptitude.html")


def hr_interview_view(request):
    return render(request, "core/hr_interview.html")


def technical_interview_view(request):
    return render(request, "core/technical_interview.html")


def results_view(request):
    return render(request, "core/results.html")


@csrf_exempt
def resume_upload_api(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    resume_file = request.FILES.get("resume")
    if not resume_file:
        return JsonResponse({"detail": "Resume file is required"}, status=400)
    request.session["resume_name"] = resume_file.name
    return JsonResponse({"status": "ok", "filename": resume_file.name})


@csrf_exempt
def aptitude_questions_api(request):
    question_type = request.GET.get("type", "mcq")
    if question_type == "code":
        return JsonResponse({"type": "code", "questions": CODE_QUESTIONS})
    return JsonResponse({"type": "mcq", "questions": MCQ_QUESTIONS})


@csrf_exempt
def aptitude_submit_api(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    payload = json.loads(request.body or "{}")
    mcq_answers = payload.get("mcq", {})
    score = 0
    for item in MCQ_QUESTIONS:
        if mcq_answers.get(str(item["id"])) == item["answer"]:
            score += 1
    max_score = len(MCQ_QUESTIONS)
    coding_submissions = payload.get("code", {})
    code_score = min(len(coding_submissions), len(CODE_QUESTIONS))
    total = score + code_score
    return JsonResponse(
        {
            "mcq_score": score,
            "mcq_total": max_score,
            "code_score": code_score,
            "code_total": len(CODE_QUESTIONS),
            "overall": total,
        }
    )


def _select_question(pool, confidence):
    if confidence >= 0.8:
        level = "hard"
    elif confidence >= 0.5:
        level = "medium"
    else:
        level = "easy"
    return random.choice(pool[level])


@csrf_exempt
def hr_chatbot_api(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    payload = json.loads(request.body or "{}")
    confidence = float(payload.get("confidence", 0.4))
    question = _select_question(HR_QUESTIONS, confidence)
    return JsonResponse({"question": question, "difficulty": "adaptive"})


@csrf_exempt
def technical_chatbot_api(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    payload = json.loads(request.body or "{}")
    confidence = float(payload.get("confidence", 0.4))
    question = _select_question(TECHNICAL_QUESTIONS, confidence)
    return JsonResponse({"question": question, "difficulty": "adaptive"})