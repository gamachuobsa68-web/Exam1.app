from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from core.db import init_db
from ui.login import LoginScreen
from ui.dashboard import DashboardScreen
from ui.teacher import TeacherScreen
from ui.admin import AdminScreen
from ui.exam import ExamScreen
from ui.leaderboard import LeaderboardScreen

class AppMain(App):
    # Global state to share logged-in user information across screens
    current_user = "Student001"
    current_role = "student"

    def build(self):
        # Initialize database tables
        init_db()

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(TeacherScreen(name="teacher"))
        sm.add_widget(AdminScreen(name="admin"))
        sm.add_widget(ExamScreen(name="exam"))
        sm.add_widget(LeaderboardScreen(name="leaderboard"))

        sm.current = "login"
        return sm

if __name__ == "__main__":
    AppMain().run()
