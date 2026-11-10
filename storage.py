import json
import os

STATE_FILE = "state.json"
BACKUP_FILE = "state.json.bak"
TEMP_FILE = "state.json.tmp"


def validate_state(data):
    """불러온 JSON 데이터의 구조와 무결성을 엄격히 검증합니다."""
    if not isinstance(data, dict):
        return False

    # 1. quizzes 검증
    quizzes = data.get("quizzes")
    if not isinstance(quizzes, list):
        return False

    for q in quizzes:
        if not isinstance(q, dict):
            return False
        
        # 필수 키 존재 및 타입/값 검증
        question = q.get("question")
        choices = q.get("choices")
        answer = q.get("answer")

        if not isinstance(question, str) or not question.strip():
            return False
        
        if not isinstance(choices, list) or len(choices) != 4:
            return False
        
        if not all(isinstance(c, str) and c.strip() for c in choices):
            return False
        
        if not isinstance(answer, int) or not (1 <= answer <= 4):
            return False

    # 2. best_score 검증 (None이거나 0~100 사이의 정수)
    best_score = data.get("best_score")
    if best_score is not None:
        if not isinstance(best_score, int) or not (0 <= best_score <= 100):
            return False

    return True


def load_state():
    """상태 데이터를 안전하게 불러오며, 손상 시 백업 파일 복구 또는 기본값 반환을 수행합니다."""
    # 1. 메인 파일 로드 시도
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if validate_state(data):
                return data
            else:
                print("⚠️ 경고: state.json 데이터 구조가 손상되었습니다.")
        except Exception as e:
            print(f"⚠️ 경고: state.json 파일을 읽는 중 오류 발생 ({e})")

    # 2. 메인 파일이 없거나 손상된 경우 백업 파일(bak) 확인
    if os.path.exists(BACKUP_FILE):
        try:
            print("🔄 백업 파일(state.json.bak)에서 복구를 시도합니다.")
            with open(BACKUP_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if validate_state(data):
                print("✅ 백업 파일 복구 성공!")
                return data
            else:
                print("⚠️ 경고: 백업 파일 데이터 구조도 손상되었습니다.")
        except Exception as e:
            print(f"⚠️ 경고: 백업 파일을 읽는 중 오류 발생 ({e})")

    # 3. 모두 실패 시 기본 빈 상태 반환 (main.py에서 DEFAULT_QUIZZES로 채워짐)
    print("ℹ️ 기본 초기 상태로 시작합니다.")
    return {"quizzes": [], "best_score": None}


def save_state(quizzes, best_score):
    """임시 파일을 거쳐 안전하게 저장하고, 성공 시 기존 파일을 백업합니다."""
    # Quiz 객체 리스트를 JSON 직렬화 가능한 딕셔너리 형태로 변환
    serialized_quizzes = []
    for q in quizzes:
        if hasattr(q, "to_dict"):
            serialized_quizzes.append(q.to_dict())
        else:
            serialized_quizzes.append({
                "question": q.question,
                "choices": q.choices,
                "answer": q.answer
            })

    data = {
        "quizzes": serialized_quizzes,
        "best_score": best_score
    }

    # 데이터 유효성 검사 후 저장
    if not validate_state(data):
        print("❌ 오류: 저장하려는 데이터의 유효성 검증에 실패했습니다. 저장을 취소합니다.")
        return

    try:
        # 1. 임시 파일(tmp)에 먼저 쓰기
        with open(TEMP_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # 2. 기존 메인 파일이 존재한다면 백업 파일(bak)로 복사 보존
        if os.path.exists(STATE_FILE):
            if os.path.exists(BACKUP_FILE):
                os.remove(BACKUP_FILE)
            os.rename(STATE_FILE, BACKUP_FILE)

        # 3. 임시 파일을 메인 파일로 교체 (Atomic Rename)
        os.rename(TEMP_FILE, STATE_FILE)

    except IOError as e:
        print(f"❌ 저장 권한 오류 또는 I/O 오류 발생: {e}")
        # 임시 파일이 남아있다면 정리
        if os.path.exists(TEMP_FILE):
            try:
                os.remove(TEMP_FILE)
            except:
                pass
    except Exception as e:
        print(f"❌ 알 수 없는 저장 오류 발생: {e}")