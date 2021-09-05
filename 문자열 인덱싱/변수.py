a = [1,2,3]
b = a
a[1] = 4
print(id(a))
print(id(b))
print(a is b)
b = a[:]
print(b)
print(a)
print(id(a))
print(id(b))

from copy import copy
a = [1,2,3]
b = copy(a)
a[1] = 4
print(a)
print(b)
a = b = 'hello'
print(a)
print(b)

a = 4
b = 1231
a,b = b,a
print(a)
print(b)
