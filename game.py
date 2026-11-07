from quiz import Quiz


DEFAULT_QUIZZES = [
    Quiz(
        "Python에서 변수를 만드는 방법으로 올바른 것은?",
        ["x = 10", "int x = 10", "let x = 10", "var x = 10"],
        1
    ),
    Quiz(
        "Python에서 문자열을 나타내는 자료형은?",
        ["int", "str", "bool", "list"],
        2
    ),
    Quiz(
        "Python에서 조건문을 만드는 키워드는?",
        ["if", "for", "while", "def"],
        1
    ),
    Quiz(
        "Python에서 반복문으로 사용할 수 있는 키워드는?",
        ["if", "for", "class", "return"],
        2
    ),
    Quiz(
        "Python에서 함수를 정의할 때 사용하는 키워드는?",
        ["func", "def", "function", "define"],
        2
    ),
]


class QuizGame:

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = input("문제를 입력하세요: ").strip()

        if question == "":
            print("⚠️ 문제를 입력하지 않았습니다. 퀴즈 추가를 취소합니다.")
            return

        choices = []

        for number in range(1, 5):
            choice = input(f"선택지 {number}: ").strip()

            if choice == "":
                print("⚠️ 선택지를 입력하지 않았습니다. 퀴즈 추가를 취소합니다.")
                return

            choices.append(choice)

        while True:
            answer_input = input("정답 번호 (1-4): ").strip()

            if answer_input == "":
                print("⚠️ 빈 입력입니다. 1-4 사이의 숫자를 입력하세요.")
                continue

            if not answer_input.isdigit():
                print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
                continue

            answer = int(answer_input)

            if answer < 1 or answer > 4:
                print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
                continue

            break

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("✅ 퀴즈가 추가되었습니다!")

    def __init__(self, quizzes=None, best_score=0):
        self.quizzes = quizzes if quizzes is not None else []
        self.best_score = best_score

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")

        correct_count = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            quiz.show(index)

            while True:
                user_input = input("정답 입력: ").strip()

                if user_input == "":
                    print("⚠️ 빈 입력입니다. 1-4 사이의 숫자를 입력하세요.")
                    continue

                if not user_input.isdigit():
                    print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
                    continue

                user_answer = int(user_input)

                if user_answer < 1 or user_answer > 4:
                    print("⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.")
                    continue

                break

            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                print("❌ 틀렸습니다!")

        score = correct_count * 20

        print("\n========================================")
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {correct_count}문제 정답! ({score}점)")
        print("========================================")

        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")