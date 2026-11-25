# (성적 관리 프로그램)

## ① 무엇을 하나요 (What)

성적 CSV 파일을 읽어 유효한 이름과 점수를 저장하고, 잘못된 데이터는 건너뛰며 해당 줄 번호와 이유를 기록하는 프로그램입니다.


## ② 왜 만들었나요 (Why)          ★ AI는 이 칸을 못 씁니다

실제 성적 파일에는 빈칸, 정수가 아닌 점수, 0~100 범위를 벗어난 점수 등이 포함될 수 있습니다. 이러한 데이터로 인해 성적 처리 과정에서 오류가 발생하는 것을 방지하고, 잘못된 입력을 쉽게 확인할 수 있도록 만들었습니다.



## ③ 어떻게 쓰나요 (How)

Python 3이 설치된 환경에서 프로젝트 폴더를 열고 다음 명령을 실행합니다.
```bash
# 설치 (테스트 도구)
python -m pip install pytest pytest-cov

# 실행
python load_scores.py scores.csv
```


## ④ 어떻게 테스트하나요

정상 입력, 예외 입력, 경계값(0점, 100점, 101점)을 확인합니다.
```bash
python -m pytest test_load_scores.py -v
python -m pytest test_load_scores.py --cov=load_scores --cov-report=term-missing
```
첫 번째 명령으로 테스트 통과 여부를 확인하고, 두 번째 명령으로 커버리지와 실행되지 않은 줄을 확인합니다.
실제 테스트 결과: [본인 터미널의 pytest 통과 화면을 붙여 넣으세요.]


## ⑤ 파일 구성

| load_scores.py | 성적 CSV 읽기 및 유효하지 않은 데이터 분류 |
| scores.csv| 성적 입력 데이터 |
| empty.csv | 헤더만 있는 파일의 테스트 데이터 | 
| weird.csv | 비정상 입력 검증용 데이터 | 
| test_load_scores.py |직접 작성한 정상·예외·경계값 단위 테스트 | 
| test_ai_A.py |코드를 AI에 제공하여 생성한 테스트 | 
| test_ai_B.py |코드를 AI에 제공하여 생성한 테스트 | 
| README.md | 프로그램 설명과 실행 및 테스트 방법 | 
| .gitignore | Git에서 제외할 파일 지정 | 

## ⑥ 만든 사람 · AI를 어디에 썼는지


- 만든 사람 : 2026100428 / 유도현
- AI를 쓴 곳 : ChatGPT를 활용하여 코드 기반 및 명세 기반 테스트를 생성·비교하고 README 초안을 작성했습니다.
- 내가 직접 판단한 것 : 명세서와 작성표