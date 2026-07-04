from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from data.questions import QUESTIONS

class TeacherScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", padding=25, spacing=15)

        self.welcome_label = Label(
            text="Teacher Question Dashboard",
            font_size=24,
            size_hint=(1, 0.15)
        )
        self.layout.add_widget(self.welcome_label)

        # Inputs to add a new question
        self.q_input = TextInput(hint_text="Enter new Question", size_hint=(1, 0.1))
        self.opt1 = TextInput(hint_text="Option A", size_hint=(1, 0.08))
        self.opt2 = TextInput(hint_text="Option B", size_hint=(1, 0.08))
        self.opt3 = TextInput(hint_text="Option C", size_hint=(1, 0.08))
        self.opt4 = TextInput(hint_text="Option D", size_hint=(1, 0.08))
        self.ans_input = TextInput(hint_text="Exact Answer text (must match one option)", size_hint=(1, 0.08))

        self.layout.add_widget(self.q_input)
        self.layout.add_widget(self.opt1)
        self.layout.add_widget(self.opt2)
        self.layout.add_widget(self.opt3)
        self.layout.add_widget(self.opt4)
        self.layout.add_widget(self.ans_input)

        # Actions Layout
        actions_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, 0.12))
        
        btn_add = Button(text="➕ Add Question", background_color=(0.18, 0.52, 0.75, 1))
        btn_add.bind(on_press=self.add_question)
        actions_layout.add_widget(btn_add)

        btn_logout = Button(text="Logout 🚪", background_color=(0.8, 0.3, 0.2, 1))
        btn_logout.bind(on_press=self.logout)
        actions_layout.add_widget(btn_logout)

        self.layout.add_widget(actions_layout)

        self.message = Label(text="", font_size=16, size_hint=(1, 0.08))
        self.layout.add_widget(self.message)

        self.add_widget(self.layout)

    def on_enter(self):
        app = App.get_running_app()
        self.welcome_label.text = f"Teacher Panel: {app.current_user}"
        self.message.text = f"Total Questions in pool: {len(QUESTIONS)}"

    def add_question(self, instance):
        q = self.q_input.text.strip()
        o1 = self.opt1.text.strip()
        o2 = self.opt2.text.strip()
        o3 = self.opt3.text.strip()
        o4 = self.opt4.text.strip()
        ans = self.ans_input.text.strip()

        if not (q and o1 and o2 and o3 and o4 and ans):
            self.message.text = "⚠️ All fields are required!"
            self.message.color = (0.8, 0.2, 0.2, 1)
            return

        if ans not in [o1, o2, o3, o4]:
            self.message.text = "⚠️ Answer must match one of the options!"
            self.message.color = (0.8, 0.2, 0.2, 1)
            return

        QUESTIONS.append({
            "question": q,
            "options": [o1, o2, o3, o4],
            "answer": ans
        })

        self.message.text = "✅ Question added successfully!"
        self.message.color = (0.2, 0.7, 0.3, 1)

        # Reset inputs
        self.q_input.text = ""
        self.opt1.text = ""
        self.opt2.text = ""
        self.opt3.text = ""
        self.opt4.text = ""
        self.ans_input.text = ""

    def logout(self, instance):
        app = App.get_running_app()
        app.current_user = ""
        app.current_role = ""
        self.manager.current = "login"
