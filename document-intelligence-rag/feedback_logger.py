import csv
import os
from datetime import datetime

FEEDBACK_FILE = "feedback_logs.csv"

def ensure_feedback_file() -> None:
    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "question",
                "answer",
                "feedback"
            ])

def log_feedback(question: str, answer: str, feedback: str) -> None:
    ensure_feedback_file()

    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().isoformat(),
            question,
            answer,
            feedback
        ])