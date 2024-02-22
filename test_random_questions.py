import unittest
from random_questions import select_random_questions

questions_bank = [
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

class TestRandomQuestions(unittest.TestCase):
    def test_select_random_questions(self):
        questions = questions_bank
        count = 5

        selected_questions = select_random_questions(questions, count)

        self.assertEqual(len(selected_questions), count)
        for question in selected_questions:
            self.assertIn(question, questions)

    # Test that the selected questions are unique
    def test_select_random_questions_unique(self):
        questions = questions_bank
        count = 5

        selected_questions = select_random_questions(questions, count)
        selected_random_questions = [question["question"] for question in selected_questions]

        self.assertEqual(len(selected_random_questions), len(set(selected_random_questions)))

    # Test that the function raises a ValueError when count is greater than the number of questions
    def test_select_random_questions_raises_value_error(self):
        questions = questions_bank
        count = 11

        with self.assertRaises(ValueError):
            select_random_questions(questions, count)

if __name__ == "__main__":
    unittest.main()
