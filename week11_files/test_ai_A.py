"""
아래 함수의 단위 테스트를 pytest로 작성해 주세요.
정상 · 예외 · 경계값을 모두 포함해 주세요.
"""
import csv

MIN_SCORE = 0
MAX_SCORE = 100


def load_scores(path):
    """성적 CSV를 읽어 (유효한 목록, 건너뛴 줄 기록) 을 돌려준다."""
    kept = []
    skipped = []

    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        for line_no, row in enumerate(reader, start=1):
            if line_no == 1:              # 헤더
                continue
            if not row:                   # 빈 줄 — 기록하지 않는다
                continue

            원본 = ",".join(row)

            if len(row) != 2:
                skipped.append((line_no, 원본, "열 개수가 2가 아님"))
                continue

            name = row[0].strip()
            raw = row[1].strip()

            if name == "":
                skipped.append((line_no, 원본, "이름이 비어 있음"))
                continue
            if raw == "":
                skipped.append((line_no, 원본, "점수가 비어 있음"))
                continue

            try:
                score = int(raw)
            except ValueError:
                skipped.append((line_no, 원본, "점수가 정수가 아님"))
                continue

            if score < MIN_SCORE or score > MAX_SCORE:
                skipped.append((line_no, 원본, "점수가 0~100 밖"))
                continue

            kept.append((name, score))

    return kept, skipped


if __name__ == "__main__":
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else "scores.csv"
    kept, skipped = load_scores(path)
    print(f"읽은 줄 : {len(kept)}개")
    for name, score in kept:
        print(f"  {name} {score}")
    print(f"건너뛴 줄 : {len(skipped)}개")
    for line_no, 원본, 이유 in skipped:
        print(f"  {line_no}행  {원본}   ← {이유}")


def test_load_scores_keeps_valid_scores_and_boundaries(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("이름,점수\n 민수 ,0\n영희,100\n", encoding="utf-8")

    kept, skipped = load_scores(path)

    assert kept == [("민수", 0), ("영희", 100)]
    assert skipped == []


def test_load_scores_records_invalid_rows_and_ignores_blank_lines(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "이름,점수\n"
        " 민수 , 50 \n"
        "\n"
        "이름만\n"
        ",90\n"
        "철수,\n"
        "영수,abc\n"
        "영희,-1\n"
        "다은,101\n"
        "잘못,1,추가\n",
        encoding="utf-8",
    )

    kept, skipped = load_scores(path)

    assert kept == [("민수", 50)]
    assert skipped == [
        (4, "이름만", "열 개수가 2가 아님"),
        (5, ",90", "이름이 비어 있음"),
        (6, "철수,", "점수가 비어 있음"),
        (7, "영수,abc", "점수가 정수가 아님"),
        (8, "영희,-1", "점수가 0~100 밖"),
        (9, "다은,101", "점수가 0~100 밖"),
        (10, "잘못,1,추가", "열 개수가 2가 아님"),
    ]


def test_load_scores_raises_for_missing_file(tmp_path):
    missing_path = tmp_path / "missing.csv"

    try:
        load_scores(missing_path)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("FileNotFoundError가 발생해야 합니다.")