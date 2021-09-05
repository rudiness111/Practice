a = ["샹크스","에드워드뉴게이트",["샬롯링링","카이도우","검은수염"]]
print(a[2][1])
a = [1, 2, 3]
b = [4, 5, 6]
print(a*3)

a = ["국어", "수학", "영어"]
a[0] = "한국사"
print(a)
a[0:2] = []
print(a)
a = ["국어", "수학", "영어"]
del a[0]
print(a)
a = ["국어", "수학", "영어"]
a.reverse ()
print(a)
a = ["국어", "수학", "영어"]
a.remove("국어")
print(a)

#문제1
#변수에 다음과 같은 문자열이 바인딩되어 있습니다.

#>>> t1 = 'python'
#>>> t2 = 'java'
#변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.

#실행 예:
#python java python java python java python java

t1= 'python'
t2= 'java'
t3= t1 + ' ' + t2+ ' '
print(t3 * 4)

#문제2
#슬라이싱을 사용해서 짝수만 출력하라.
#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])


