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

    # state에서 불러온 best_score가 없거나 초기 상태일 때 None을 허용하여 처리
    initial_best_score = state.get("best_score", None)

    # game 객체를 try문 바깥에서 생성하여 예외 처리에서도 접근 가능하도록 설정
    game = QuizGame(quizzes, initial_best_score)

    try:
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

    except KeyboardInterrupt:
        print("\n⚠️ 키보드 인터럽트가 감지되었습니다.")

    except EOFError:
        print("\n⚠️ 입력이 종료되었습니다.")

    finally:
        # 프로그램이 어떤 이유로든 종료될 때(Ctrl+C 포함) 현재 상태를 안전하게 저장
        try:
            game.save()
            print("💾 프로그램 종료 전 현재 상태가 안전하게 저장되었습니다.")
        except Exception as e:
            print(f"❌ 저장 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()