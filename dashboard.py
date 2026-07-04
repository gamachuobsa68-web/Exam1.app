from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        self.welcome_label = Label(
            text="Welcome to Oro Exam Dashboard",
            font_size=24,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.welcome_label)

        btn_start = Button(text="Start Exam", size_hint=(1, 0.15))
        btn_start.bind(on_press=self.start_exam)
        self.layout.add_widget(btn_start)

        btn_leaderboard = Button(text="Leaderboard", size_hint=(1, 0.15))
        btn_leaderboard.bind(on_press=self.view_leaderboard)
        self.layout.add_widget(btn_leaderboard)

        btn_logout = Button(text="Logout", size_hint=(1, 0.15))
        btn_logout.bind(on_press=self.logout)
        self.layout.add_widget(btn_logout)

        self.add_widget(self.layout)

    def on_enter(self):
        app = App.get_running_app()
        self.welcome_label.text = f"Welcome, {app.current_user}! (Role: {app.current_role})"

    def start_exam(self, instance):
        self.manager.current = "exam"

    def view_leaderboard(self, instance):
        self.manager.current = "leaderboard"

    def logout(self, instance):
        app = App.get_running_app()
        app.current_user = "Student001"
        app.current_role = "student"
        self.manager.current = "login"
