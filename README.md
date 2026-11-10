# 나만의 퀴즈 게임

Python으로 만든 콘솔 기반 퀴즈 게임입니다.

## 프로젝트 개요

사용자가 퀴즈를 풀고, 새 퀴즈를 추가하고, 등록된 퀴즈를 확인하며, 최고 점수를 저장하는 프로그램입니다.

프로그램을 종료한 뒤 다시 실행해도 추가한 퀴즈와 최고 점수는 `state.json`에 저장되어 유지됩니다.

## 퀴즈 주제 선정 이유

Python 기초 문법을 복습할 수 있도록 Python 관련 퀴즈를 주제로 선정했습니다.

## 실행 방법

```bash
python main.py
```

## 기능 목록

- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록
- 점수 확인
- 종료
- 잘못된 입력 처리
- 데이터 저장 및 불러오기

## 파일 구조

```text
main.py
quiz.py
game.py
storage.py
state.json
README.md
.gitignore
docs/
```

## 데이터 파일 설명

`state.json`은 퀴즈 데이터와 최고 점수를 저장합니다.

```json
{
  "quizzes": [
    {
      "question": "Python에서 함수를 정의할 때 사용하는 키워드는?",
      "choices": ["func", "def", "function", "define"],
      "answer": 2
    }
  ],
  "best_score": 80
}
```

- `quizzes`: 퀴즈 목록
- `question`: 문제
- `choices`: 선택지 4개
- `answer`: 정답 번호
- `best_score`: 최고 점수

## 커밋 메시지 규칙

형식: 종류: 변경 내용 요약

- Feat: 새로운 기능
- Fix: 오류 수정
- Refactor: 동작을 유지하면서 구조 개선
- Docs: 문서 작성 및 수정
- Test: 테스트 추가 및 검증 기록

예시:
- Feat: 퀴즈 목록 조회 기능 구현
- Fix: 0점과 미플레이 상태 구분
- Docs: 데이터 복구 절차 작성

## 설계 및 검증 자료

- [클래스 설계와 변경 영향 범위](docs/design.md)
- [입력·저장·종료 테스트 결과](docs/test-results.md)
- [Git 커밋·브랜치·clone·pull 기록](docs/git-workflow.md)

- clone 및 pull 실습을 완료했습니다.