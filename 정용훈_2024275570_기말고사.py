import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows의 경우 '맑은 고딕' 폰트 사용
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 파일 경로 설정 (경로에 특수 문자가 포함된 경우 raw string으로 변경)
path_2020 = r'C:\Users\마공주\Downloads\성동구립도서관 장서 대출목록 (2020년 11월).csv'
path_2023 = r'C:\Users\마공주\Downloads\성동구립도서관 장서 대출목록 (2023년 11월).csv'

# 데이터 불러오기
try:
    data_2020 = pd.read_csv(path_2020)
    data_2023 = pd.read_csv(path_2023)
except FileNotFoundError as e:
    print(f"파일을 찾을 수 없습니다: {e}")
    exit()

# 데이터 확인: 첫 몇 줄과 컬럼명을 출력
print("2020년 데이터 컬럼명:", data_2020.columns)
print("2023년 데이터 컬럼명:", data_2023.columns)
print("2020년 데이터 첫 줄:\n", data_2020.head())
print("2023년 데이터 첫 줄:\n", data_2023.head())

# 전처리: 중복 제거 및 누락값 처리
data_2020.drop_duplicates(inplace=True)
data_2023.drop_duplicates(inplace=True)
data_2020.dropna(inplace=True)
data_2023.dropna(inplace=True)

# (1) 2020년 11월과 비교하여 2023년 11월 시점에서 추가된 도서의 목록 및 개수
added_books = data_2023[~data_2023['도서명'].isin(data_2020['도서명'])]
added_books_count = added_books.shape[0]

# (2) 2020년 11월과 비교하여 2023년 11월 시점에서 없어진 도서의 목록 및 개수
removed_books = data_2020[~data_2020['도서명'].isin(data_2023['도서명'])]
removed_books_count = removed_books.shape[0]

# (3) 2020년 11월과 2023년 11월 가장 대출이 많이 발생한 도서 상위 20권의 리스트와 그 빈도수 비교
top_20_books_2020 = data_2020['도서명'].value_counts().head(20)
top_20_books_2023 = data_2023['도서명'].value_counts().head(20)

# (4) 2020년 11월과 2023년 11월 가장 대출이 많이 발생한 도서 상위 100권 중 동일한 도서의 리스트와 그 개수
top_100_books_2020 = set(data_2020['도서명'].value_counts().head(100).index)
top_100_books_2023 = set(data_2023['도서명'].value_counts().head(100).index)
common_top_100_books = top_100_books_2020.intersection(top_100_books_2023)
common_top_100_books_count = len(common_top_100_books)

# (5) 2020년 11월 가장 대출이 많이 발생한 도서 상위 50권의 당시 대출 횟수와 현재 대출 횟수 비교하여 증가한 도서와 감소한 도서 파악, 그래프로 표현
top_50_books_2020 = data_2020['도서명'].value_counts().head(50)
top_50_books_2023_counts = data_2023['도서명'].value_counts()

# 인덱스가 존재하지 않는 경우 0으로 채우기
top_50_books_comparison = pd.DataFrame({
    '2020': top_50_books_2020,
    '2023': top_50_books_2023_counts.reindex(top_50_books_2020.index, fill_value=0)
})

top_50_books_comparison['Difference'] = top_50_books_comparison['2023'] - top_50_books_comparison['2020']

# 증가한 도서와 감소한 도서 파악
increased_books = top_50_books_comparison[top_50_books_comparison['Difference'] > 0]
decreased_books = top_50_books_comparison[top_50_books_comparison['Difference'] < 0]

# 그래프로 표현
plt.figure(figsize=(12, 8))
top_50_books_comparison.sort_values('Difference', inplace=True)
top_50_books_comparison['Difference'].plot(kind='barh', color='skyblue')
plt.title('Top 50 Borrowed Books: Difference in Borrow Counts (2023 vs 2020)')
plt.xlabel('Difference in Borrow Counts')
plt.ylabel('Books')
plt.show()

# (6) 추가 분석 - 상위 100권 도서의 평균 대출 횟수 비교
mean_borrow_2020 = data_2020['도서명'].value_counts().head(100).mean()
mean_borrow_2023 = data_2023['도서명'].value_counts().head(100).mean()

# 결과 출력
print(f"2023년 11월 시점에서 추가된 도서의 개수: {added_books_count}")
print(f"2023년 11월 시점에서 없어진 도서의 개수: {removed_books_count}")
print("\n2020년 11월 상위 20권 도서 대출 횟수:\n", top_20_books_2020)
print("\n2023년 11월 상위 20권 도서 대출 횟수:\n", top_20_books_2023)
print(f"\n2020년과 2023년 상위 100권 중 동일한 도서의 개수: {common_top_100_books_count}")
print("\n2020년 상위 50권 도서의 대출 횟수 비교:\n", top_50_books_comparison)
print(f"\n상위 100권 도서의 평균 대출 횟수 비교: 2020년 - {mean_borrow_2020}, 2023년 - {mean_borrow_2023}")
