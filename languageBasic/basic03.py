# strip()메서드 : 문자열에서 앞뒤 공백이나 특정 문자를 제거하는 데 사용

s = "  Hello World  "
print(s.strip())  # "Hello World"

ss = "--Hel--lo--"
print(ss.strip('-'))  # "Hel--lo"

price = '1,234원'
print(price[:-1]) # 1,234   문자열의 처음부터 마지막 문자 바로 앞까지를 선택, 마지막 문자를 제외한 모든 부분을 가져옴
print(price[-1]) # 원       마지막 문자
print(price[1:]) # ,234원   첫 번째 문자부터 끝까지
# price[start:end]
# start: 시작 인덱스 (생략하면 0부터 시작)
# end: 끝 인덱스 (생략하면 문자열 끝까지)
# 음수 인덱스는 뒤에서부터 센 위치를 의미.
