from game import QuizGame, DEFAULT_QUIZZES
from quiz import Quiz
from storage import load_state


def show_menu():
    print("========================================")
    print("🎯 나만의 퀴즈 게임 🎯")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")


def get_menu_choice():
    while True:
        choice = input("선택: ").strip()

        if choice == "":
            print("⚠️ 빈 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        if not choice.isdigit():
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        number = int(choice)

        if number < 1 or number > 5:
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            continue

        return number


def main():
    state = load_state()

    quizzes = []

    for quiz_data in state["quizzes"]:
        quizzes.append(
            Quiz(
                quiz_data["question"],
                quiz_data["choices"],
                quiz_data["answer"]
            )
        )

    if not quizzes:
        quizzes = DEFAULT_QUIZZES

    game = QuizGame(quizzes, state["best_score"])

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            game.play_quiz()
            game.save()
        elif choice == 2:
            game.add_quiz()
            game.save()
        elif choice == 3:
            game.show_quiz_list()
        elif choice == 4:
            game.show_best_score()
        elif choice == 5:
            game.save()
            print("👋 프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n⚠️ 프로그램을 안전하게 종료합니다.")

    except EOFError:
        print("\n⚠️ 입력이 종료되어 프로그램을 안전하게 종료합니다.")