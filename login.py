from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

from core.auth import login_user

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        self.title = Label(
            text="🎓 ORO EXAM LOGIN",
            font_size=28,
            size_hint=(1, 0.25),
            color=(0.18, 0.52, 0.75, 1) # Beautiful sky blue
        )

        self.role = Spinner(
            text="student",
            values=("student", "teacher", "admin"),
            size_hint=(1, 0.15)
        )

        self.username = TextInput(
            hint_text="Username",
            multiline=False,
            size_hint=(1, 0.15)
        )

        self.password = TextInput(
            hint_text="Password",
            password=True,
            multiline=False,
            size_hint=(1, 0.15)
        )

        self.message = Label(
            text="",
            font_size=16,
            color=(0.8, 0.2, 0.2, 1), # Red by default for errors
            size_hint=(1, 0.15)
        )

        btn = Button(
            text="LOGIN",
            size_hint=(1, 0.15),
            background_color=(0.18, 0.52, 0.75, 1)
        )
        btn.bind(on_press=self.check_login)

        layout.add_widget(self.title)
        layout.add_widget(self.role)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(btn)
        layout.add_widget(self.message)

        self.add_widget(layout)

    def check_login(self, instance):
        role_selected = self.role.text
        user_val = self.username.text.strip()
        pass_val = self.password.text.strip()

        ok = login_user(role_selected, user_val, pass_val)

        if ok:
            self.message.color = (0.2, 0.7, 0.3, 1) # Green
            self.message.text = "Login Successful ✔"
            
            # Save user session details in App main instance
            app = App.get_running_app()
            app.current_user = user_val
            app.current_role = role_selected

            # Reset fields for security
            self.username.text = ""
            self.password.text = ""
            self.message.text = ""

            if role_selected == "student":
                self.manager.current = "dashboard"
            elif role_selected == "teacher":
                self.manager.current = "teacher"
            elif role_selected == "admin":
                self.manager.current = "admin"
        else:
            self.message.color = (0.8, 0.2, 0.2, 1) # Red
            self.message.text = "Invalid username or password ❌"
