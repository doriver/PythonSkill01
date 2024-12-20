if 4 in [1,2,3,4]: print("if문 작동 4가 있따")

languages = ['python', 'perl', 'c', 'java']

for lang in languages :
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")

                    # enumerate는 각 요소와 함께 해당 요소의 인덱스를 반환
for idx, language in enumerate(languages, start=1):
    print(f"{idx}. {language}")
    # f-string: 문자열 포매팅 방법 중 하나로, 중괄호 {} 안에 변수나 표현식을 삽입할 수 있다.