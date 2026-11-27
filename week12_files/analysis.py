import pandas as pd


# 1. 데이터 정제
def 정제(df):
    print("시작", len(df))

    # 빈 칸 제거
    df = df.dropna(subset=["점수"])
    print("빈 칸 제거", len(df))

    # 중복 제거
    df = df.drop_duplicates()
    print("중복 제거", len(df))

    # 반과 과목의 앞뒤 공백 제거
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()

    # 점수가 0~100 범위 밖인 행 제거
    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))

    return df


# 2. 반별 평균
def 반별평균(df):
    return df.groupby("반")["점수"].mean()


if __name__ == "__main__":

    # 3. CSV 파일 불러오기 및 정제
    df = pd.read_csv("scores_2026.csv")
    df = 정제(df)

    print("반 종류:", sorted(df["반"].unique()))
    print("과목 종류:", sorted(df["과목"].unique()))

    # 4. 필터링
    수학 = df[df["과목"] == "수학"]

    print("\n[필터링]")
    print("수학 행 수:", len(수학))

    # 5. 그룹화
    print("\n[반별 평균]")
    print(반별평균(df).round(2))

    print("\n[과목별·반별 평균]")
    print(df.groupby(["과목", "반"])["점수"].mean().round(2))

    # 6. 반별 통계
    print("\n[반별 통계]")
    print(df.groupby("반")["점수"].agg(
        ["count", "mean", "median", "max"]
    ).round(2))

    # 7. 합계 일치 검증
    print("\n[합계 일치 검증]")

    그룹합계 = df.groupby("반")["점수"].sum().sum()
    전체합계 = df["점수"].sum()

    print("그룹별 합계의 합:", 그룹합계)
    print("전체 합계:", 전체합계)
    print("일치 여부:", 그룹합계 == 전체합계)

    # 8. 개수 일치 검증
    print("\n[개수 일치 검증]")

    그룹개수 = df.groupby("반")["점수"].count().sum()
    전체개수 = len(df)

    print("그룹별 개수의 합:", 그룹개수)
    print("전체 행 수:", 전체개수)
    print("일치 여부:", 그룹개수 == 전체개수)

    # 9. 스팟 체크
    print("\n[스팟 체크: 1반 수학]")

    점수 = df[(df["반"] == "1반") &
              (df["과목"] == "수학")]["점수"]

    print("점수 목록:", 점수.tolist())
    print("점수 합계:", 점수.sum())
    print("점수 개수:", len(점수))
    print("직접 계산한 평균:", 점수.sum() / len(점수))

    그룹평균 = df.groupby(["과목", "반"])["점수"].mean()

    print("그룹화 평균:", 그룹평균.loc[("수학", "1반")])
    print("일치 여부:",
          점수.sum() / len(점수) ==
          그룹평균.loc[("수학", "1반")])
