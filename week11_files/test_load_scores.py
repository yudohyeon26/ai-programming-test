from pathlib import Path

import pytest
from load_scores import load_scores

BASE_DIR = Path(__file__).resolve().parent


# 정상 ① 정상 파일 읽기
def test_정상_파일을_읽는다():
    kept, skipped = load_scores(BASE_DIR / "scores.csv")
    assert len(kept) == 5


# 정상 ② 빈 줄 건너뛰기
def test_빈_줄은_건너뛴다(tmp_path):
    path = tmp_path / "blank.csv"
    path.write_text(
        "이름,점수\n김하나,88\n\n이민수,90\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)
    assert kept == [("김하나", 88), ("이민수", 90)]
    assert skipped == []


# 정상 ③ 이름에 쉼표가 있는 경우
def test_이름에_쉼표가_있어도_읽는다(tmp_path):
    path = tmp_path / "comma.csv"
    path.write_text(
        '이름,점수\n"김,하나",88\n',
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)
    assert kept == [("김,하나", 88)]
    assert skipped == []


# 예외 ① 존재하지 않는 파일
def test_없는_파일이면_오류가_난다(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_scores(tmp_path / "없는파일.csv")


# 예외 ② 헤더만 있는 파일
def test_헤더만_있으면_빈_결과가_나온다():
    kept, skipped = load_scores(BASE_DIR / "empty.csv")
    assert kept == []
    assert skipped == []


# 경계값 테스트
@pytest.mark.parametrize("점수, 유효한가", [
    (-1, False),
    (0, True),
    (1, True),
    (99, True),
    (100, True),
    (101, False),
])
def test_점수_경계값(tmp_path, 점수, 유효한가):
    path = tmp_path / "boundary.csv"
    path.write_text(
        f"이름,점수\n김하나,{점수}\n",
        encoding="utf-8"
    )

    kept, skipped = load_scores(path)

    if 유효한가:
        assert kept == [("김하나", 점수)]
        assert skipped == []
    else:
        assert kept == []
        assert len(skipped) == 1
