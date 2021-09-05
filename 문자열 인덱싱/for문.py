import mark as mark

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a :
    print(first)
    print(last)
(a,b) = (1,2)

marks = [90, 23, 32, 67, 76]
number = 0
for marks in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격 입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

