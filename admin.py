from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
import sqlite3
from core.db import DB, init_db

class AdminScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", padding=35, spacing=20)

        self.welcome_label = Label(
            text="Admin Control Panel",
            font_size=28,
            size_hint=(1, 0.2)
        )
        self.layout.add_widget(self.welcome_label)

        # Control utilities
        btn_reset = Button(text="🧹 Reset Results Database", size_hint=(1, 0.15), background_color=(0.8, 0.3, 0.2, 1))
        btn_reset.bind(on_press=self.reset_database)
        self.layout.add_widget(btn_reset)

        btn_info = Button(text="📋 Database Statistics Overview", size_hint=(1, 0.15), background_color=(0.18, 0.52, 0.75, 1))
        btn_info.bind(on_press=self.show_db_stats)
        self.layout.add_widget(btn_info)

        btn_logout = Button(text="Logout 🚪", size_hint=(1, 0.15))
        btn_logout.bind(on_press=self.logout)
        self.layout.add_widget(btn_logout)

        self.message = Label(text="", font_size=16, size_hint=(1, 0.2))
        self.layout.add_widget(self.message)

        self.add_widget(self.layout)

    def on_enter(self):
        app = App.get_running_app()
        self.welcome_label.text = f"Admin Console: {app.current_user}"
        self.message.text = "Authorized administrative access only."

    def reset_database(self, instance):
        try:
            conn = sqlite3.connect(DB)
            c = conn.cursor()
            c.execute("DROP TABLE IF EXISTS results")
            conn.commit()
            conn.close()
            init_db()
            self.message.text = "✅ Results database table reset successfully!"
            self.message.color = (0.2, 0.7, 0.3, 1)
        except Exception as e:
            self.message.text = f"❌ Error: {str(e)}"
            self.message.color = (0.8, 0.2, 0.2, 1)

    def show_db_stats(self, instance):
        try:
            conn = sqlite3.connect(DB)
            c = conn.cursor()
            c.execute("SELECT COUNT(*), AVG(score) FROM results")
            count, avg_score = c.fetchone()
            conn.close()
            
            avg_val = round(avg_score, 2) if avg_score is not None else 0
            self.message.text = f"📊 Total Attempts: {count}\n📊 Average Score: {avg_val} correct answers"
            self.message.color = (0.9, 0.9, 0.9, 1)
        except Exception as e:
            self.message.text = f"❌ Error: {str(e)}"
            self.message.color = (0.8, 0.2, 0.2, 1)

    def logout(self, instance):
        app = App.get_running_app()
        app.current_user = ""
        app.current_role = ""
        self.manager.current = "login"
