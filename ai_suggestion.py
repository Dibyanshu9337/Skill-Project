import random

def get_ai_suggestion(text):
    text = text.lower()

    # Keyword-based mental health responses
    responses = {
        "sad": [
            "I'm really sorry you're feeling sad. It's okay to feel this way sometimes.",
            "Sad days happen, but they don’t define you. Be gentle with yourself.",
            "Try doing one small thing that makes you feel even slightly better."
        ],
        "depressed": [
            "You’re not alone in feeling this way.",
            "It might help to talk to someone you trust about how you’re feeling.",
            "Small steps matter. Even getting out of bed is progress."
        ],
        "anxious": [
            "Take a slow deep breath. Inhale... hold... exhale.",
            "Anxiety can feel overwhelming, but it will pass.",
            "Try grounding yourself by noticing 5 things around you."
        ],
        "stress": [
            "Stress is tough, but you’re stronger than you think.",
            "Break your task into small manageable steps.",
            "Give yourself permission to rest."
        ],
        "lonely": [
            "Feeling lonely can be hard. You matter more than you realize.",
            "Consider reaching out to a friend or family member.",
            "You're not alone here — I'm listening."
        ],
        "happy": [
            "That's wonderful! Keep spreading the positivity 😊",
            "I'm glad you're feeling happy today!",
            "Celebrate even small wins!"
        ]
    }

    # Check for keywords
    for keyword in responses:
        if keyword in text:
            return random.choice(responses[keyword])

    # Default fallback response
    return "Thank you for sharing how you feel. Remember, your feelings are valid and important."