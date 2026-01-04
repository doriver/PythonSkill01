import pandas as pd

# 리스트 또는 배열로 Series생성
# data01 = [10, 20, 30]
# s01 = pd.Series(data01)
# print(s01)

# 딕셔너로리 Series생성
data02 = {"a": 10, "b":20, "c":30}
s02 = pd.Series(data02)
print(s02)
# print(s02.values) # [10 20 30]
# print(s02.index) # Index(['a', 'b', 'c'], dtype='object')
# print(s02.dtype) # int64

# 인덱스를 사용해 값 선택
print(s02['a']) # 10
# 위치를 사용해 값 선택
print(s02.iloc[0]) # 10

# 조건 필터링
print(s02[ s02 > 15 ]) # 부분Series
# 산술연산
print(s02 + 5) # 각 원소에 5 더해짐