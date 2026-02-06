MCQ_QUESTIONS = [
    {
        "id": 1,
        "question": "Which Python data type is immutable?",
        "options": ["list", "dict", "set", "tuple"],
        "answer": "tuple",
        "skill_tag": "python",
        "difficulty": "easy",
    },
    {
        "id": 2,
        "question": "What does REST stand for?",
        "options": [
            "Representational State Transfer",
            "Reliable Endpoint System Test",
            "Remote Execution Service Tool",
            "Randomized Encryption Session Token",
        ],
        "answer": "Representational State Transfer",
        "skill_tag": "api",
        "difficulty": "easy",
    },
    {
        "id": 3,
        "question": "Which HTTP status code means 'Unauthorized'?",
        "options": ["200", "401", "403", "500"],
        "answer": "401",
        "skill_tag": "security",
        "difficulty": "easy",
    },
    {
        "id": 4,
        "question": "What is the primary purpose of Django's ORM?",
        "options": [
            "To compile Python code",
            "To map Python classes to database tables",
            "To manage CSS styling",
            "To deploy containers",
        ],
        "answer": "To map Python classes to database tables",
        "skill_tag": "django",
        "difficulty": "medium",
    },
    {
        "id": 5,
        "question": "Which JavaScript method converts JSON to an object?",
        "options": ["JSON.parse", "JSON.stringify", "JSON.convert", "JSON.object"],
        "answer": "JSON.parse",
        "skill_tag": "javascript",
        "difficulty": "easy",
    },
    {
        "id": 6,
        "question": "What does CSRF protection help prevent?",
        "options": [
            "Cross-Site Request Forgery",
            "Cross-Server Remote Fetch",
            "Client-Side Resource Failure",
            "Cached Session Randomization",
        ],
        "answer": "Cross-Site Request Forgery",
        "skill_tag": "security",
        "difficulty": "medium",
    },
    {
        "id": 7,
        "question": "Which SQL clause is used to filter results?",
        "options": ["ORDER BY", "WHERE", "GROUP BY", "LIMIT"],
        "answer": "WHERE",
        "skill_tag": "database",
        "difficulty": "easy",
    },
    {
        "id": 8,
        "question": "What is the output of len({'a': 1, 'b': 2}) in Python?",
        "options": ["1", "2", "3", "4"],
        "answer": "2",
        "skill_tag": "python",
        "difficulty": "easy",
    },
    {
        "id": 9,
        "question": "Which tool is used to create vector embeddings?",
        "options": ["spaCy", "Sentence Transformers", "FAISS", "TensorBoard"],
        "answer": "Sentence Transformers",
        "skill_tag": "ml",
        "difficulty": "medium",
    },
    {
        "id": 10,
        "question": "What is the main goal of RAG systems?",
        "options": [
            "Generate images",
            "Retrieve context to ground AI responses",
            "Compress databases",
            "Replace REST APIs",
        ],
        "answer": "Retrieve context to ground AI responses",
        "skill_tag": "ml",
        "difficulty": "medium",
    },
]

CODE_QUESTIONS = [
    {
        "id": 1,
        "prompt": "Write a function that returns the first non-repeating character in a string.",
        "skill_tag": "python",
        "difficulty": "medium",
        "expected": "Uses a frequency map and returns the first unique char",
    },
    {
        "id": 2,
        "prompt": "Design a REST API endpoint for submitting interview answers with a JSON schema.",
        "skill_tag": "api",
        "difficulty": "easy",
        "expected": "Explains endpoint, method, payload, and response",
    },
    {
        "id": 3,
        "prompt": "Explain how you would optimize a Django query for a large dataset.",
        "skill_tag": "django",
        "difficulty": "medium",
        "expected": "Mentions select_related, prefetch_related, indexes",
    },
]

HR_QUESTIONS = {
    "easy": [
        "Walk me through your resume in 60 seconds.",
        "What motivates you at work?",
    ],
    "medium": [
        "Tell me about a time you handled conflict on a team.",
        "How do you prioritize tasks when everything feels urgent?",
    ],
    "hard": [
        "Describe a failure and what you learned from it.",
        "How would you influence stakeholders who disagree with your approach?",
    ],
}

TECHNICAL_QUESTIONS = {
    "easy": [
        "Explain the difference between a list and a tuple in Python.",
        "What is REST and why is it useful?",
    ],
    "medium": [
        "How would you design a resume parsing pipeline with spaCy?",
        "Explain how vector search helps in RAG systems.",
    ],
    "hard": [
        "Describe how you'd scale a Django + DRF system for 1M users.",
        "How do you evaluate confidence in an AI interview response?",
    ],
}