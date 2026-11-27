import pandas as pd

df = pd.read_csv("scores_2026.csv")

print("전체 행·열:", df.shape)
print("빈 칸:", df["점수"].isna().sum())
print("중복:", df.duplicated().sum())
print("반 이름 종류:", df["반"].unique())
print("과목 이름 종류:", df["과목"].unique())
print(df["점수"].describe())