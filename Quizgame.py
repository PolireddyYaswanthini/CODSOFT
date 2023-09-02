import tkinter as tk
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.configure(bg="#4CAF50")  # Set background color
        self.root.geometry("2000x2000")
        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["A) Paris", "B) London", "C) Berlin"],
                "correct_answer": "A"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": ["A) Earth", "B) Mars", "C) Venus"],
                "correct_answer": "B"
            },
            {
                "question": "What is the largest mammal in the world?",
                "choices": ["A) Elephant", "B) Giraffe", "C) Blue Whale"],
                "correct_answer": "C"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["A) Go", "B) Au", "C) Ag"],
                "correct_answer": "B"
            }
        ]

        self.current_question = -1
        self.user_score = 0

        self.welcome_label = tk.Label(root, text="Welcome to the Quiz Game!", font=("Helvetica", 16), bg="#4CAF50", fg="white")
        self.welcome_label.pack(pady=10)

        self.rules_label = tk.Label(root, text="Rules:\n1. Select the correct option (A, B, or C) for each question.\n2. You will receive feedback on your answer.", font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.rules_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Quiz", font=("Helvetica", 12), command=self.start_quiz, bg="#008CBA", fg="white")
        self.start_button.pack(pady=10)

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#4CAF50", fg="white")
        self.question_label.pack(pady=10)

        self.choice_buttons = []
        for i in range(3):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            button.pack()
            self.choice_buttons.append(button)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.feedback_label.pack(pady=10)

        self.next_question_button = tk.Button(root, text="Next Question", font=("Helvetica", 12), state=tk.DISABLED, command=self.next_question, bg="#008CBA", fg="white")
        self.next_question_button.pack(pady=10)

    def start_quiz(self):
        self.welcome_label.pack_forget()
        self.rules_label.pack_forget()
        self.start_button.pack_forget()
        self.show_next_question()

    def show_next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, choice in enumerate(question_data["choices"]):
                self.choice_buttons[i].config(text=choice)
            self.feedback_label.config(text="")
            self.next_question_button.config(state=tk.DISABLED)
        else:
            self.question_label.config(text="Quiz Completed!")
            self.feedback_label.config(text=f"Your Score: {self.user_score}/{len(self.questions)}")
            performance = self.calculate_performance()
            self.feedback_label.config(text=f"Your Score: {self.user_score}/{len(self.questions)}\nPerformance: {performance}")
            for button in self.choice_buttons:
                button.config(state=tk.DISABLED)
            self.next_question_button.config(state=tk.DISABLED)

    def check_answer(self, choice_index):
        question_data = self.questions[self.current_question]
        user_choice = chr(ord('A') + choice_index)
        if user_choice == question_data["correct_answer"]:
            self.feedback_label.config(text="Correct!", fg="lightgreen")
            self.user_score += 1
        else:
            self.feedback_label.config(text=f"Incorrect. Correct Answer: {question_data['correct_answer']}", fg="red")
        self.next_question_button.config(state=tk.NORMAL)

    def calculate_performance(self):
        score = self.user_score
        total_questions = len(self.questions)
        if score == total_questions:
            return "Excellent"
        elif score >= total_questions * 0.7:
            return "Good"
        elif score >= total_questions * 0.5:
            return "Average"
        else:
            return "Poor"

    def next_question(self):
        self.show_next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
