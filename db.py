import sqlite3

DB = "exam.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        student TEXT,
        score INTEGER,
        total INTEGER
    )
    """)
    conn.commit()
    conn.close()

def save_result(student, score, total):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        student TEXT,
        score INTEGER,
        total INTEGER
    )
    """)
    c.execute("""
    INSERT INTO results VALUES (?, ?, ?)
    """, (student, score, total))
    conn.commit()
    conn.close()

def get_results():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    try:
        c.execute("SELECT student, score, total FROM results ORDER BY score DESC")
        data = c.fetchall()
    except sqlite3.OperationalError:
        data = []
    conn.close()
    return data
