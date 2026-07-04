from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App

import random

from data.questions import QUESTIONS
from core.logic import grade_exam
from core.db import save_result
from utils.pdf import generate_result_pdf

class ExamScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = None

    def on_enter(self):
        # Reset questions state on entering a new exam
        self.index = 0
        self.answers = {}
        self.questions = QUESTIONS.copy()
        random.shuffle(self.questions)

        # Clear existing widgets to build a clean exam layout
        self.clear_widgets()

        self.layout = BoxLayout(orientation="vertical", padding=25, spacing=15)

        self.question_label = Label(text="", font_size=20, size_hint=(1, 0.3), halign="center")

        self.option_buttons = []
        for i in range(4):
            btn = Button(size_hint=(1, 0.12))
            btn.bind(on_press=self.select_answer)
            self.option_buttons.append(btn)

        self.next_btn = Button(text="NEXT ➡", size_hint=(1, 0.15), background_color=(0.1, 0.6, 0.2, 1))
        self.next_btn.bind(on_press=self.next_question)

        self.layout.add_widget(self.question_label)
        for b in self.option_buttons:
            self.layout.add_widget(b)
        self.layout.add_widget(self.next_btn)

        self.add_widget(self.layout)
        self.load_question()

    def load_question(self):
        q = self.questions[self.index]
        self.question_label.text = f"Question {self.index + 1}/{len(self.questions)}

{q['question']}"
        
        # Reset button visual styles and populate texts
        for i, opt in enumerate(q["options"]):
            btn = self.option_buttons[i]
            btn.text = opt
            if self.index in self.answers and self.answers[self.index] == opt:
                btn.background_color = (0.18, 0.52, 0.75, 1) # Highlight blue
            else:
                btn.background_color = (1, 1, 1, 1) # Normal

        # If it is the last question, change Next button text
        if self.index == len(self.questions) - 1:
            self.next_btn.text = "FINISH EXAM 🏁"
            self.next_btn.background_color = (0.8, 0.3, 0.2, 1)
        else:
            self.next_btn.text = "NEXT ➡"
            self.next_btn.background_color = (0.1, 0.6, 0.2, 1)

    def select_answer(self, instance):
        # Store answer and update visual indicators instantly
        self.answers[self.index] = instance.text
        for btn in self.option_buttons:
            if btn.text == instance.text:
                btn.background_color = (0.18, 0.52, 0.75, 1) # Blue
            else:
                btn.background_color = (1, 1, 1, 1) # Reset other buttons

    def next_question(self, instance):
        if self.index < len(self.questions) - 1:
            self.index += 1
            self.load_question()
        else:
            self.finish_exam()

    def finish_exam(self):
        score, total = grade_exam(self.answers, self.questions)
        
        # Pull real logged-in student name from App session
        app = App.get_running_app()
        student_name = app.current_user if app.current_user else "Student001"

        # Save result to database
        save_result(student_name, score, total)

        # Generate report PDF
        generate_result_pdf(student_name, score, total)

        # Redirect back to dashboard
        self.manager.current = "dashboard"
