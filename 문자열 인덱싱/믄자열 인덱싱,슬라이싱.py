a = 'Life is too short \nYou need python'
print(a[2])
print(a[-1])
print(a[:8])
print(a[8:])
print(a[::2])

#문제1
#letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
단어 = 'letters'
print(단어[0], 단어[2])

#문제2
#letters을 거꾸로 뒤집어 출력하세요.
a = 'letters'
print(a[::-1])

#문제 3
#홀짝홀짝홀짝에서 '홀' 만 출력하세요.
a = '홀짝홀짝홀짝'
print(a[0],a[2],a[4]) #이거 말고
print(a[::2]) #요렇게 하면 더 편하다
