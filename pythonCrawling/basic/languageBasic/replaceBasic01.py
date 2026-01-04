str = "asdlkfjl \r\n ㅁㄴㅇㅁㄴㅇ \r\n alskdfjlaksjl214j12409uasdfasdklfjald \r\n alsdjflkwerpwriqp21312 \r\n 123123123123"

print(str)
print(" replace 적용시킬꺼 ")

print(str.replace('\r\n', '<br>'))
print(str.replace("\r\n", "<br>"))


str02 = "asdlkfjl \n ㅁㄴㅇㅁㄴㅇ \n alskdfjlaksjl214j12409uasdfasdklfjald \n alsdjflkwerpwriqp21312 \n 123123123123"
print(str02)
print(" replace 적용시킬꺼 ")

print(str02.replace('\n', '<br>'))
print(str02.replace("\n", "<br>"))