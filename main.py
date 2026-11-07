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
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 5:
            print("👋 프로그램을 종료합니다.")
            break

        print("아직 구현되지 않은 기능입니다.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ 프로그램을 안전하게 종료합니다.")
    except EOFError:
        print("\n⚠️ 입력이 종료되어 프로그램을 안전하게 종료합니다.")