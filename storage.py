import json
import os

STATE_FILE = "state.json"


def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "quizzes": [],
            "best_score": 0
        }

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("⚠️ 저장 파일을 읽을 수 없어 기본 데이터로 초기화합니다.")

        return {
            "quizzes": [],
            "best_score": 0
        }


def save_state(quizzes, best_score):
    data = {
        "quizzes": [],
        "best_score": best_score
    }

    for quiz in quizzes:
        data["quizzes"].append({
            "question": quiz.question,
            "choices": quiz.choices,
            "answer": quiz.answer
        })

    try:
        with open(STATE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except OSError:
        print("⚠️ 저장 파일에 데이터를 저장하지 못했습니다.")