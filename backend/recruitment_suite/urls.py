from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("aptitude/", views.aptitude_view, name="aptitude"),
    path("interview/hr/", views.hr_interview_view, name="hr-interview"),
    path("interview/technical/", views.technical_interview_view, name="technical-interview"),
    path("results/", views.results_view, name="results"),
    path("api/resume/upload/", views.resume_upload_api, name="resume-upload"),
    path("api/aptitude/questions/", views.aptitude_questions_api, name="aptitude-questions"),
    path("api/aptitude/submit/", views.aptitude_submit_api, name="aptitude-submit"),
    path("api/chatbot/hr/", views.hr_chatbot_api, name="hr-chatbot"),
    path("api/chatbot/technical/", views.technical_chatbot_api, name="technical-chatbot"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)