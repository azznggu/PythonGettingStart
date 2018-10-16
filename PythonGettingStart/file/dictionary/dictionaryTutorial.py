x = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
print(x)


# 키 중복 시에는 가장 뒤에 값만 저장됨.
x = {'a':10, 'a':20, 'c':30, 'd':40, 'e':50}
print(x)

# 키 - 리스트, 딕셔너리 제외한 타입 가능.   값- 모든 자료형 가능.
x = {100:'hundred', False:0, 3.5:[1,2,3]}
print(x)

#딕셔너리 생성

x = {}
print(x)
y = dict()
print(y)


#1. 딕셔너리 = dict(키1=값2, 키2=값2)
x1 = dict(a=1, b=2, c=3)
print(x1)
#2. 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
x2 = dict(zip(['a','b','c'],[1,2,3]))
print(x2)
#3. 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
x3 = dict([('a',1),('b',2),('c',3)])
print(x3)
#4. 딕셔너리 = dict({키2: 값1, 키2: 값2})
x4 = dict({'a':1,'b':2,'c':3})
print(x4)


#응용
x5 = dict(zip(range(1,11), [2** i for i in range(1,11)]))
print(x5)


# 키 접근, 할당
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
print(x['a'])

x = {100:'hundred', False:0, 3.5:[1,2,3]}
print(x[False])
print(x[3.5])


x = {'a': 10, 'b': 20, 'c': 30}
x['a'] = 100
print(x)


# 키 개수 -> len

print(len(x))

#응용
x = dict(zip(range(123,234),list(str(i) for i in range(123,234))))
print(x)
print(len(x))




