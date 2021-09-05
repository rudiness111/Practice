a = "I need %d apples" % 3
b= "I eat " + str(3) + "apples"
print(a)
print(b)
number = 10
day = "three"
a= "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)
a= "asdasdjasljdlasjdlasj {}lasjdlasjdlasjldasjlasldaa".format("안녕")
print(a)
name= "int"
a= "나의 이름은 {int} 입니다"
print(a)
a= "hobby"
print(a.find('b'))
print(a.find('x'))
a= ",".join("abcd")
print(a)
a= "hi"
print(a.lower())
a = "Life is too short"
print(a.replace("Life", "Your leg"))
a = "a:b:c:d"
print(a.split(":"))


#문제1
#아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
#string = 'abcdfe2a354a32a'
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

#문제2
#아래 코드의 실행 결과를 예상해보세요.

>> string = 'abcd'
>> string.replace('b', 'B')
>> print(string)

#답: 'abcd'는 문자열이기 떄문에 'aBcd'로 바뀌지 않고, 그대로 'abcd'로 출력된다.
