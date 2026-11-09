# codyssey2

C:\codyssey2>cd c:\codyssey2      

c:\codyssey2>git status
fatal: not a git repository (or any of the parent directories): .git

c:\codyssey2>git init
Initialized empty Git repository in C:/codyssey2/.git/

c:\codyssey2>git remote add origin https://github.com/jdspecialist/codyssey2.git

c:\codyssey2>git remote -v
origin  https://github.com/jdspecialist/codyssey2.git (fetch)
origin  https://github.com/jdspecialist/codyssey2.git (push)

c:\codyssey2>git fetch origin
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 7 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (7/7), 3.77 KiB | 94.00 KiB/s, done.
From https://github.com/jdspecialist/codyssey2
 * [new branch]      main       -> origin/main

c:\codyssey2>git branch -M main

c:\codyssey2>git pull origin main --allow-unrelated-histories
From https://github.com/jdspecialist/codyssey2
 * branch            main       -> FETCH_HEAD
error: The following untracked working tree files would be overwritten by merge:
        .gitignore
        README.md
Please move or remove them before you merge.
Aborting

c:\codyssey2>git pull origin main --allow-unrelated-histories
From https://github.com/jdspecialist/codyssey2
 * branch            main       -> FETCH_HEAD

c:\codyssey2>git add .

c:\codyssey2>git commit -m "Feat: 프로젝트 초기 구조 및 README 작성"
On branch main
nothing to commit, working tree clean

c:\codyssey2>git push -u origin main
branch 'main' set up to track 'origin/main'.
Everything up-to-date

c:\codyssey2>notepad main.py

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

c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: abc
⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.
선택: 9
⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.
선택: 엔터
⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.
선택: 1
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.

c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.py

nothing added to commit but untracked files present (use "git add" to track)

c:\codyssey2>git add main.py

c:\codyssey2>git commit -m "Feat: 메뉴 화면과 종료 기능 구현"
[main 5b6b944] Feat: 메뉴 화면과 종료 기능 구현
 1 file changed, 52 insertions(+)
 create mode 100644 main.py

c:\codyssey2>git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 895 bytes | 99.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/jdspecialist/codyssey2.git
   912b897..5b6b944  main -> main

c:\codyssey2>notepad quiz.py

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self, number):
        print(f"\n[문제 {number}]")
        print(self.question)

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


c:\codyssey2>git add quiz.py

c:\codyssey2>git commit -m "Feat: Quiz 클래스 및 문제 출력·정답 확인 기능 구현"
[main 933906b] Feat: Quiz 클래스 및 문제 출력·정답 확인 기능 구현
 1 file changed, 15 insertions(+)
 create mode 100644 quiz.py

c:\codyssey2>git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 548 bytes | 8.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jdspecialist/codyssey2.git
   5b6b944..933906b  main -> main

c:\codyssey2>notepad game.py

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

c:\codyssey2>notepad game.py

c:\codyssey2>git add game.py

c:\codyssey2>git commit -m "Feat: Python 기초 기본 퀴즈 5개 추가"
[main a7cf769] Feat: Python 기초 기본 퀴즈 5개 추가
 1 file changed, 29 insertions(+)
 create mode 100644 game.py


c:\codyssey2>git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 655 bytes | 93.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jdspecialist/codyssey2.git
   933906b..a7cf769  main -> main

   
c:\codyssey2>git checkout -b feature/play-quiz
Switched to a new branch 'feature/play-quiz'

# game.py에 내용 추가

class QuizGame:
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

# main.py의 main 함수에 추가

from game import QuizGame, DEFAULT_QUIZZES


def main():
    game = QuizGame(DEFAULT_QUIZZES)

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            game.play_quiz()
        elif choice == 5:
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("아직 구현되지 않은 기능입니다.")

## 
c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1

📝 퀴즈를 시작합니다! (총 5문제)

[문제 1]
Python에서 변수를 만드는 방법으로 올바른 것은?
1. x = 10
2. int x = 10
3. let x = 10
4. var x = 10
정답 입력: 2
❌ 틀렸습니다!

[문제 2]
Python에서 문자열을 나타내는 자료형은?
1. int
2. str
3. bool
4. list
정답 입력: 1
❌ 틀렸습니다!

[문제 3]
Python에서 조건문을 만드는 키워드는?
1. if
2. for
3. while
4. def
정답 입력: 1
✅ 정답입니다!

[문제 4]
Python에서 반복문으로 사용할 수 있는 키워드는?
1. if
2. for
3. class
4. return
정답 입력: 2
✅ 정답입니다!

[문제 5]
Python에서 함수를 정의할 때 사용하는 키워드는?
1. func
2. def
3. function
4. define
정답 입력: 3
❌ 틀렸습니다!

========================================
🏆 결과: 5문제 중 2문제 정답! (40점)
========================================
🎉 새로운 최고 점수입니다!
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.

c:\codyssey2>git add game.py main.py

c:\codyssey2>git commit -m "Feat: 퀴즈 출제 및 정답 판정 기능 구현"
[feature/play-quiz 533674c] Feat: 퀴즈 출제 및 정답 판정 기능 구현
 2 files changed, 63 insertions(+), 4 deletions(-)

c:\codyssey2>git checkout main
M       README.md
Switched to branch 'main'
Your branch is up to date with 'origin/main'.


c:\codyssey2>git merge feature/play-quiz
Updating a7cf769..533674c
Fast-forward
 game.py | 54 +++++++++++++++++++++++++++++++++++++++++++++++++++++-
 main.py | 13 ++++++++++---
 2 files changed, 63 insertions(+), 4 deletions(-)

c:\codyssey2>git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.48 KiB | 251.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/jdspecialist/codyssey2.git
   a7cf769..533674c  main -> main


c:\codyssey2>notepad main.py

c:\codyssey2>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 50AD-60EB

 c:\codyssey2 디렉터리

2026-11-07  오후 01:34    <DIR>          .
2026-11-07  오후 12:37             4,884 .gitignore
2026-11-07  오후 12:14    <DIR>          .qodo
2026-11-07  오후 01:34             2,619 game.py
2026-11-07  오후 01:41             1,519 main.py
2026-11-07  오후 12:45               451 quiz.py
2026-11-07  오후 01:34            13,495 README.md
2026-11-07  오후 01:02    <DIR>          __pycache__
               5개 파일              22,968 바이트
               3개 디렉터리   6,540,410,880 바이트 남음

c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 


c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 2
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 3
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 4
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.

c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")

c:\codyssey2>git add main.py

c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   main.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md


c:\codyssey2>git commit -m "Feat: 메뉴 화면과 종료 기능 구현"
[main e280086] Feat: 메뉴 화면과 종료 기능 구현
 1 file changed, 3 insertions(+), 10 deletions(-)

c:\codyssey2>git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 352 bytes | 50.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/jdspecialist/codyssey2.git
   533674c..e280086  main -> main

c:\codyssey2>notepad main.py

c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 2
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 3
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 4
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.

c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

c:\codyssey2>git add main.py

c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

c:\codyssey2>git commit -m "Feat: 메뉴 화면과 종료 기능 구현"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

c:\codyssey2>git push origin main
Everything up-to-date


c:\codyssey2>notepad quiz.py

c:\codyssey2>class Quiz:
'class'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다.

c:\codyssey2>notepad quiz.py

c:\codyssey2>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: 50AD-60EB

 c:\codyssey2 디렉터리

2026-11-07  오후 01:34    <DIR>          .
2026-11-07  오후 12:37             4,884 .gitignore
2026-11-07  오후 12:14    <DIR>          .qodo
2026-11-07  오후 01:34             2,619 game.py
2026-11-07  오후 01:41             1,519 main.py
2026-11-07  오후 01:56               451 quiz.py
2026-11-07  오후 01:52            20,874 README.md
2026-11-07  오후 01:02    <DIR>          __pycache__
               5개 파일              30,347 바이트
               3개 디렉터리   6,240,804,864 바이트 남음

c:\codyssey2>python -c "from quiz import Quiz; q = Quiz('테스트 문제', ['A', 'B', 'C', 'D'], 2); q.show(1); print(q.is_correct(2))"

[문제 1]
테스트 문제
1. A
2. B
3. C
4. D
True

c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

c:\codyssey2>git add quiz.py

c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

c:\codyssey2>git commit -m "Feat: Quiz 클래스 및 문제 출력·정답 확인 기능 구현"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

c:\codyssey2>git push origin main
Everything up-to-date

c:\codyssey2>notepad quiz.py

c:\codyssey2>python -c "from quiz import Quiz; q = Quiz('테스트 문제', ['A', 'B', 'C', 'D'], 2); q.show(1); print(q.is_correct(2))"

[문제 1]
테스트 문제
1. A
2. B
3. C
4. D
True

c:\codyssey2>notepad game.py

c:\codyssey2>notepad main.py

c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1

📝 퀴즈를 시작합니다! (총 5문제)

[문제 1]
Python에서 변수를 만드는 방법으로 올바른 것은?
1. x = 10
2. int x = 10
3. let x = 10
4. var x = 10
정답 입력: 2
❌ 틀렸습니다!

[문제 2]
Python에서 문자열을 나타내는 자료형은?
1. int
2. str
3. bool
4. list
정답 입력: 1
❌ 틀렸습니다!

[문제 3]
Python에서 조건문을 만드는 키워드는?
1. if
2. for
3. while
4. def
정답 입력: 1
✅ 정답입니다!

[문제 4]
Python에서 반복문으로 사용할 수 있는 키워드는?
1. if
2. for
3. class
4. return
정답 입력: 2
✅ 정답입니다!

[문제 5]
Python에서 함수를 정의할 때 사용하는 키워드는?
1. func
2. def
3. function
4. define
정답 입력: 3
❌ 틀렸습니다!

========================================
🏆 결과: 5문제 중 2문제 정답! (40점)
========================================
🎉 새로운 최고 점수입니다!
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.


c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   game.py
        modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")

c:\codyssey2>git add game.py main.py

c:\codyssey2>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   game.py
        modified:   main.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md


c:\codyssey2>git commit -m "Feat: 퀴즈 출제 및 정답 판정 기능 구현"
[main ffad2b1] Feat: 퀴즈 출제 및 정답 판정 기능 구현
 2 files changed, 12 insertions(+), 3 deletions(-)

c:\codyssey2>git push origin main
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 599 bytes | 85.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/jdspecialist/codyssey2.git
   e280086..ffad2b1  main -> main

c:\codyssey2>git checkout -b feature/add-quiz
Switched to a new branch 'feature/add-quiz'

c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1

📝 퀴즈를 시작합니다! (총 5문제)

[문제 1]
Python에서 변수를 만드는 방법으로 올바른 것은?
1. x = 10
2. int x = 10
3. let x = 10
4. var x = 10
정답 입력: 2
❌ 틀렸습니다!

[문제 2]
Python에서 문자열을 나타내는 자료형은?
1. int
2. str
3. bool
4. list
정답 입력: 3
❌ 틀렸습니다!

[문제 3]
Python에서 조건문을 만드는 키워드는?
1. if
2. for
3. while
4. def
정답 입력: 4
❌ 틀렸습니다!

[문제 4]
Python에서 반복문으로 사용할 수 있는 키워드는?
1. if
2. for
3. class
4. return
정답 입력: 5
⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.
정답 입력: 6
⚠️ 잘못된 입력입니다. 1-4 사이의 숫자를 입력하세요.
정답 입력: 3
❌ 틀렸습니다!

[문제 5]
Python에서 함수를 정의할 때 사용하는 키워드는?
1. func
2. def
3. function
4. define
정답 입력: 3
❌ 틀렸습니다!

========================================
🏆 결과: 5문제 중 0문제 정답! (0점)
========================================
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 2
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 2
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1

📝 퀴즈를 시작합니다! (총 5문제)

[문제 1]
Python에서 변수를 만드는 방법으로 올바른 것은?
1. x = 10
2. int x = 10
3. let x = 10
4. var x = 10
정답 입력: 2
❌ 틀렸습니다!

[문제 2]
Python에서 문자열을 나타내는 자료형은?
1. int
2. str
3. bool
4. list
정답 입력: 2
✅ 정답입니다!

[문제 3]
Python에서 조건문을 만드는 키워드는?
1. if
2. for
3. while
4. def
정답 입력: 2
❌ 틀렸습니다!

[문제 4]
Python에서 반복문으로 사용할 수 있는 키워드는?
1. if
2. for
3. class
4. return
정답 입력: 2
✅ 정답입니다!

[문제 5]
Python에서 함수를 정의할 때 사용하는 키워드는?
1. func
2. def
3. function
4. define
정답 입력: 2
✅ 정답입니다!

========================================
🏆 결과: 5문제 중 3문제 정답! (60점)
========================================
🎉 새로운 최고 점수입니다!
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 3
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 4
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 2
아직 구현되지 않은 기능입니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.

c:\codyssey2>git add game.py main.py

c:\codyssey2>git commit -m "Feat: 퀴즈 추가 기능 구현"
[feature/add-quiz da5ace4] Feat: 퀴즈 추가 기능 구현
 1 file changed, 45 insertions(+)

c:\codyssey2>git checkout main
M       README.md
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

c:\codyssey2>git merge feature/add-quiz
Updating ffad2b1..da5ace4
Fast-forward
 game.py | 45 +++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 45 insertions(+)

c:\codyssey2>git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 787 bytes | 112.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/jdspecialist/codyssey2.git
   ffad2b1..da5ace4  main -> main

c:\codyssey2>notepad game.py


c:\codyssey2>python main.py
Traceback (most recent call last):
  File "c:\codyssey2\main.py", line 1, in <module>
    from game import QuizGame, DEFAULT_QUIZZES
  File "c:\codyssey2\game.py", line 40
        while question == "":
    ^
TabError: inconsistent use of tabs and spaces in indentation

c:\codyssey2>
c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.

c:\codyssey2>python -m py_compile main.py game.py quiz.py

c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 3

📋 등록된 퀴즈 목록
[1] Python에서 변수를 만드는 방법으로 올바른 것은?
[2] Python에서 문자열을 나타내는 자료형은?
[3] Python에서 조건문을 만드는 키워드는?
[4] Python에서 반복문으로 사용할 수 있는 키워드는?
[5] Python에서 함수를 정의할 때 사용하는 키워드는?

총 5개의 퀴즈가 등록되어 있습니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 3

📋 등록된 퀴즈 목록
[1] Python에서 변수를 만드는 방법으로 올바른 것은?
[2] Python에서 문자열을 나타내는 자료형은?
[3] Python에서 조건문을 만드는 키워드는?
[4] Python에서 반복문으로 사용할 수 있는 키워드는?
[5] Python에서 함수를 정의할 때 사용하는 키워드는?

총 5개의 퀴즈가 등록되어 있습니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 4

🏆 최고 점수 확인
현재 최고 점수: 0점
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 2

📌 새로운 퀴즈를 추가합니다.
문제를 입력하세요: 노벨상 수상자가 아닌 사람은?
선택지 1: 제프리 힌턴
선택지 2: 데미스 허사비스             
선택지 3: 존 점퍼
선택지 4: 일리야 수츠케버
정답 번호 (1-4): 4
✅ 퀴즈가 추가되었습니다!
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 1

📝 퀴즈를 시작합니다! (총 6문제)

[문제 1]
Python에서 변수를 만드는 방법으로 올바른 것은?
1. x = 10
2. int x = 10
3. let x = 10
4. var x = 10
정답 입력: 1
✅ 정답입니다!

[문제 2]
Python에서 문자열을 나타내는 자료형은?
1. int
2. str
3. bool
4. list
정답 입력: 1
❌ 틀렸습니다!

[문제 3]
Python에서 조건문을 만드는 키워드는?
1. if
2. for
3. while
4. def
정답 입력: 1
✅ 정답입니다!

[문제 4]
Python에서 반복문으로 사용할 수 있는 키워드는?
1. if
2. for
3. class
4. return
정답 입력: 1
❌ 틀렸습니다!

[문제 5]
Python에서 함수를 정의할 때 사용하는 키워드는?
1. func
2. def
3. function
4. define
정답 입력: 1
❌ 틀렸습니다!

[문제 6]
노벨상 수상자가 아닌 사람은?
1. 제프리 힌턴
2. 데미스 허사비스
3. 존 점퍼
4. 일리야 수츠케버
정답 입력: 4
✅ 정답입니다!

========================================
🏆 결과: 6문제 중 3문제 정답! (50점)
========================================
🎉 새로운 최고 점수입니다!
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 3

📋 등록된 퀴즈 목록
[1] Python에서 변수를 만드는 방법으로 올바른 것은?
[2] Python에서 문자열을 나타내는 자료형은?
[3] Python에서 조건문을 만드는 키워드는?
[4] Python에서 반복문으로 사용할 수 있는 키워드는?
[5] Python에서 함수를 정의할 때 사용하는 키워드는?
[6] 노벨상 수상자가 아닌 사람은?

총 6개의 퀴즈가 등록되어 있습니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 4

🏆 최고 점수 확인
현재 최고 점수: 50점
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.


c:\codyssey2>python -c "from game import QuizGame; print(hasattr(QuizGame, 'show_quizzes')); print(hasattr(QuizGame, 'show_best_score'))"
True
True

c:\codyssey2>python -m py_compile main.py game.py quiz.py

c:\codyssey2>python main.py
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 3

📋 등록된 퀴즈 목록
[1] Python에서 변수를 만드는 방법으로 올바른 것은?
[2] Python에서 문자열을 나타내는 자료형은?
[3] Python에서 조건문을 만드는 키워드는?
[4] Python에서 반복문으로 사용할 수 있는 키워드는?
[5] Python에서 함수를 정의할 때 사용하는 키워드는?

총 5개의 퀴즈가 등록되어 있습니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 3

📋 등록된 퀴즈 목록
[1] Python에서 변수를 만드는 방법으로 올바른 것은?
[2] Python에서 문자열을 나타내는 자료형은?
[3] Python에서 조건문을 만드는 키워드는?
[4] Python에서 반복문으로 사용할 수 있는 키워드는?
[5] Python에서 함수를 정의할 때 사용하는 키워드는?

총 5개의 퀴즈가 등록되어 있습니다.
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 4

🏆 최고 점수 확인
현재 최고 점수: 0점
========================================
🎯 나만의 퀴즈 게임 🎯
========================================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
========================================
선택: 5
👋 프로그램을 종료합니다.
