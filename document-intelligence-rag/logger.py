import csv
import os
from datetime import datetime

LOG_FILE = "rag_logs.csv"

def ensure_log_file() -> None:
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "question",
                "answer",
                "relevance_score",
                "context_match"
            ])

def log_interaction(question: str, answer: str, evaluation: dict) -> None:
    ensure_log_file()

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().isoformat(),
            question,
            answer,
            evaluation.get("relevance_score"),
            evaluation.get("context_match")
        ])