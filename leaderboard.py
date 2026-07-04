from core.db import get_results
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class LeaderboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", padding=25, spacing=15)

        self.title = Label(text="🏆 Leaderboard", font_size=32, size_hint=(1, 0.15))
        self.layout.add_widget(self.title)

        self.box = BoxLayout(orientation="vertical", spacing=5, size_hint=(1, 0.7))
        self.layout.add_widget(self.box)

        # Back to Dashboard button (CRITICAL NAVIGATION ADDITION)
        self.btn_back = Button(text="⬅ Back to Dashboard", size_hint=(1, 0.15))
        self.btn_back.bind(on_press=self.go_back)
        self.layout.add_widget(self.btn_back)

        self.add_widget(self.layout)

    def on_enter(self):
        self.box.clear_widgets()
        results = get_results()

        if not results:
            self.box.add_widget(
                Label(text="No exam attempts registered yet. Be the first!", font_size=18, color=(0.7, 0.7, 0.7, 1))
            )
            return

        rank = 1
        for student, score, total in results:
            percentage = int((score / total) * 100) if total > 0 else 0
            self.box.add_widget(
                Label(
                    text=f"Rank {rank}: {student} — Score: {score}/{total} ({percentage}%)",
                    font_size=18,
                    color=(0.9, 0.9, 0.9, 1)
                )
            )
            rank += 1

    def go_back(self, instance):
        self.manager.current = "dashboard"
