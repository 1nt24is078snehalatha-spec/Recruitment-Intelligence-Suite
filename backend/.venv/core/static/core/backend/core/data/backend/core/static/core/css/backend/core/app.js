const resumeForm = document.querySelector("#resume-upload");
const resumeStatus = document.querySelector("#resume-status");

if (resumeForm) {
    resumeForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const formData = new FormData(resumeForm);
        const response = await fetch("/api/resume/upload/", {
            method: "POST",
            body: formData,
        });
        const data = await response.json();
        if (response.ok) {
            resumeStatus.textContent = `Uploaded: ${data.filename}`;
        } else {
            resumeStatus.textContent = data.detail || "Upload failed";
        }
    });
}

const questionContainer = document.querySelector("#question-container");
const loadMcq = document.querySelector("#load-mcq");
const loadCode = document.querySelector("#load-code");
const submitAptitude = document.querySelector("#submit-aptitude");
const aptitudeResult = document.querySelector("#aptitude-result");
const pauseButton = document.querySelector("#pause-test");
const resumeButton = document.querySelector("#resume-test");

let mcqAnswers = JSON.parse(localStorage.getItem("mcqAnswers") || "{}");
let codeAnswers = JSON.parse(localStorage.getItem("codeAnswers") || "{}");
let isPaused = localStorage.getItem("aptitudePaused") === "true";

function renderMcq(questions) {
    questionContainer.innerHTML = "";
    questions.forEach((item) => {
        const wrapper = document.createElement("div");
        wrapper.className = "card";
        const options = item.options
            .map(
                (option) =>
                    `<label><input type="radio" name="q-${item.id}" value="${option}" ${
                        mcqAnswers[item.id] === option ? "checked" : ""
                    }> ${option}</label>`
            )
            .join("");
        wrapper.innerHTML = `<h4>${item.question}</h4><div class="form-grid">${options}</div>`;
        wrapper.querySelectorAll("input").forEach((input) => {
            input.addEventListener("change", () => {
                mcqAnswers[item.id] = input.value;
                localStorage.setItem("mcqAnswers", JSON.stringify(mcqAnswers));
            });
        });
        questionContainer.appendChild(wrapper);
    });
}

function renderCode(questions) {
    questionContainer.innerHTML = "";
    questions.forEach((item) => {
        const wrapper = document.createElement("div");
        wrapper.className = "card";
        wrapper.innerHTML = `
            <h4>${item.prompt}</h4>
            <textarea rows="5" placeholder="Type your solution or approach...">${
                codeAnswers[item.id] || ""
            }</textarea>
        `;
        const textarea = wrapper.querySelector("textarea");
        textarea.addEventListener("input", () => {
            codeAnswers[item.id] = textarea.value;
            localStorage.setItem("codeAnswers", JSON.stringify(codeAnswers));
        });
        questionContainer.appendChild(wrapper);
    });
}

async function loadQuestions(type) {
    if (isPaused) {
        aptitudeResult.textContent = "Resume the test to load questions.";
        return;
    }
    const response = await fetch(`/api/aptitude/questions/?type=${type}`);
    const data = await response.json();
    if (type === "mcq") {
        renderMcq(data.questions);
    } else {
        renderCode(data.questions);
    }
}

if (loadMcq) {
    loadMcq.addEventListener("click", () => loadQuestions("mcq"));
}

if (loadCode) {
    loadCode.addEventListener("click", () => loadQuestions("code"));
}

if (pauseButton) {
    pauseButton.addEventListener("click", () => {
        isPaused = true;
        localStorage.setItem("aptitudePaused", "true");
        aptitudeResult.textContent = "Test paused. Resume to continue.";
    });
}

if (resumeButton) {
    resumeButton.addEventListener("click", () => {
        isPaused = false;
        localStorage.setItem("aptitudePaused", "false");
        aptitudeResult.textContent = "Test resumed.";
    });
}

if (submitAptitude) {
    submitAptitude.addEventListener("click", async () => {
        const response = await fetch("/api/aptitude/submit/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mcq: mcqAnswers, code: codeAnswers }),
        });
        const data = await response.json();
        aptitudeResult.textContent = `MCQ ${data.mcq_score}/${data.mcq_total} | Code ${data.code_score}/${data.code_total} | Overall ${data.overall}`;
    });
}

function attachChat(formId, windowId, apiUrl, warningId) {
    const form = document.querySelector(formId);
    const chatWindow = document.querySelector(windowId);
    const warning = document.querySelector(warningId);
    if (!form || !chatWindow) {
        return;
    }
    let confidence = 0.4;

    const addBubble = (text, type) => {
        const bubble = document.createElement("div");
        bubble.className = `chat-bubble ${type}`;
        bubble.textContent = text;
        chatWindow.appendChild(bubble);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    };

    addBubble("Hi! Let's begin. Share a quick introduction.", "bot");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const input = form.querySelector("input");
        const value = input.value.trim();
        if (!value) {
            return;
        }
        addBubble(value, "user");
        input.value = "";
        confidence = Math.min(0.95, Math.max(0.2, confidence + (value.length > 40 ? 0.1 : -0.05)));
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ confidence, message: value }),
        });
        const data = await response.json();
        addBubble(data.question, "bot");
    });

    form.addEventListener("paste", () => {
        warning.textContent = "Copy/paste detected. Please answer in your own words.";
    });
}

attachChat("#hr-chat-form", "#chat-window", "/api/chatbot/hr/", "#hr-warning");
attachChat("#tech-chat-form", "#tech-chat-window", "/api/chatbot/technical/", "#tech-warning");

let tabSwitchCount = 0;
const tabWarningLimit = 3;

window.addEventListener("visibilitychange", () => {
    if (document.hidden) {
        tabSwitchCount += 1;
        const warningMessage = `Warning: Tab switch detected (${tabSwitchCount}/${tabWarningLimit}).`;
        const warnings = document.querySelectorAll(".warning");
        warnings.forEach((warning) => {
            warning.textContent = warningMessage;
        });
        if (tabSwitchCount >= tabWarningLimit) {
            warnings.forEach((warning) => {
                warning.textContent = "Disqualified due to excessive tab switching.";
            });
        }
    }
});     