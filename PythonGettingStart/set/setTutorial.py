#set - 집합

#set 요소는 순서 없음.
s = {'a','b','c','d','e'}
print(s)
print(s)

#set 요소는 중복 불가.
s = {'a','a','c','d','e'}
#중복요소 넣어도 실제로는 하나만..
print(s)


#리스트,튜플, 딕셔너리와 달리 특정 요소 접근 불가 ex) list[0] tuple[1] dictionary[key]
#s[0] -> TypeError: 'set' object does not support indexing
#s['a'] -> TypeError: 'set' object is not subscriptable




#set 생성  set(반복가능객체)

a = set('apple')
print(a)

b = set(range(10))
print(b)

c = set()
print(c)


#dictionary와 다름 주의
d = {}
print(type(d))
s = set()
print(type(s))


#변경 불가 세트 = frozenset

f = frozenset(range(10))
