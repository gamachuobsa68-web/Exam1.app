# 🎓 Oro Exam System

Professional Exam Management System built using Kivy (Python) and ReportLab.

This workspace contains both the **Fully Corrected and Enhanced Python/Kivy source files** and an **interactive React web-based live simulator** that mirrors the complete functionality of the application in your browser!

## Features
- **Student Login**: Secure authentication for students to access exams (`student1` / `1234` or `student2` / `1234`).
- **Teacher Panel**: Manage questions (add and validate new questions) and monitor question pool size (`teacher1` / `1234`).
- **Admin Panel**: Statistics overview (total attempts, average score) and reset scores database (`admin` / `admin123`).
- **MCQ Exam Engine**: Complete interactive multiple choice test with randomized questions, real-time visual selection indicators, and automatic grading.
- **PDF Report Generator**: Automatically generates high-quality result certificates on completion.
- **SQLite Database**: Persistent relational storage for results and exam configurations.
- **Real-Time Leaderboard**: Dynamically updated ranking based on score percentage with fallback empty states.

## Installation
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python main.py
```
