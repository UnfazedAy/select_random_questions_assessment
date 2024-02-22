import random
from typing import List, Dict

def select_random_questions(questions: List[Dict], count: int) -> List[Dict]:
    """
    Selects a random set of questions from a list of questions.

    Args:
    questions: list of questions
    count: number of questions to select

    Returns:
    list: random set of questions
    """
    if count > len(questions):
        raise ValueError("Count cannot be greater than the number of questions.")
    
    selected_random_questions = random.sample(questions, count)
    return selected_random_questions


if __name__ == "__main__":
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the capital of Germany?", "answer": "Berlin"},
        {"question": "What is the capital of Italy?", "answer": "Rome"},
        {"question": "What is the capital of Spain?", "answer": "Madrid"},
        {"question": "What is the capital of Portugal?", "answer": "Lisbon"},
        {"question": "What is the capital of Greece?", "answer": "Athens"},
        {"question": "What is the capital of Sweden?", "answer": "Stockholm"},
        {"question": "What is the capital of Norway?", "answer": "Oslo"},
        {"question": "What is the capital of Finland?", "answer": "Helsinki"},
        {"question": "What is the capital of Denmark?", "answer": "Copenhagen"}
    ]

    selected_questions = select_random_questions(questions, 5)
    i = 1
    for question in selected_questions:
        print(f"Question {i}: {question['question']} Answer: {question['answer']}")
        i += 1