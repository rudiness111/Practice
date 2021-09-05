from typing import List

dic = {'name': '김규원', 'age':17}
print(dic['name'])

a= {1: 'a'}
a[2] = 'b'
print(a)
a = {1:'국어', 2:'수학', 3:'영어'}
print(a)
print(a.keys())
print(a.values())
print(a.items())
for k in a.values():
    print(k)
#키: str(k)
#밸류: v
a.clear()
print(a)
a = {1:'국어', 2:'수학', 3:'영어'}
print(a[1])
print(a.get(4))
print(a.get(4,'없음'))
print(4 in a)
print(1 in a)

#문제1
#다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
#icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레', '월드콘': 1500, '메로나': 1000)
price =list(icecream.values())
print(price)
