#tuple
a = 1,'b',4.5, False
#a = (1,'b',4.5, False)

print(a)

#tuple접근->index.
print(a[3])

#tuple길이
print(str(len(a)))

#but tuple은 요소 변경 불가. 읽기전용.(tuple' object does not support item assignment)
#a[0] = 2  -> TypeError발생.


#1개짜리 or empty tuple -> 함수에 tuple 넣어야할 경우 사용.

#값 1개짜리 tuple 선언 시 ','필수.
single = 1,
print(single)

#빈 tuple
empty = ()
empty =tuple()


#tuple사용한 tuple생성
a = tuple([1,2,3])
print(a)
a = tuple(range(10))
print(a)
a = tuple(range(5,12))
print(a)
a = tuple(range(10,0,-1))
print(a)
a = tuple(range(10,20,2))
print(a)


#tuple -> list
tlist1 = list((1,2,3))
print(tlist1)
tlist2 = list(tuple(range(10)))
print(tlist2)


#리스트와 튜플로 변수 만들기
#리스트와 튜플을 사용하면 변수 여러 개를 한 번에 만들 수 있음
a,b,c = [1,2,3]
print(a,b,c)
d,e,f = (4,5,6)
print(d,e,f)

#변수로도 가능,
x = [1,2,3]
a,b,c = x
print(a,b,c)
y = (4,5,6)
d,e,f = y
print(d,e,f)



