import pandas as pd
from analysis import 정제, 반별평균


본 = 정제(pd.read_csv("scores_2026.csv"))
미니 = 정제(pd.read_csv("mini.csv"))


# 1. 정제 후 행 수 검증
def test_정제하면_100행이_남는다():
    assert len(본) == 100


# 2. 반 이름의 공백 제거 검증
def test_반은_두_종류만_남는다():
    assert sorted(본["반"].unique()) == ["1반", "2반"]


# 3. 그룹별 합계와 전체 합계 일치 검증
def test_그룹합이_전체합과_같다():
    assert 본.groupby("반")["점수"].sum().sum() == 본["점수"].sum()


# 4. 손계산 결과와 코드 결과 비교
def test_손계산과_일치한다():
    assert 반별평균(미니)["1반"] == 80.0
