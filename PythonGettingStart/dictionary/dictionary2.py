x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

#update - 키 값 갱신
x.update(a=100)
print(x)
x.update(a='aa', b=False)
print(x['a'],x['b'])

#pop - 특정 키-값 쌍 삭제 후 삭제 값 반환. pop(키) or pop(키,값)
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
popped = x.pop('a')
print(popped)

#기본값 지정. 키가 없을 때는 기본값만 반환
popped = x.pop('f','not exists')
print(popped)

#내장함수 del로도 키-값 삭제 가능.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
print(x)

#popitem - 파이썬 3.6 이상에서는 맨 뒤에 있는 값을 삭제.그리고 삭제된 키-값 쌍을 튜플로 반환합니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
popped = x.popitem()
print(popped)

#clear -모두 삭제
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)

#get - 특정 키 값 반환, 없을 시 지정 기본 값 반환
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
got = x.get('a','not exist')
print(got)
got = x.get('f','not exist')
print(got)

#setdefault - 키,값 추가. 키만 지정시 none저장..
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e',50)
print(x)

#items
print(x.items())
#keys
print(x.keys())
#values
print(x.values())

#fromkeys - 리스트,튜플 요소를 키로 딕셔너리 생성. 기본값지정 가능.
keys = ('a','b','c','d','e')
x = dict.fromkeys(keys)
print(x)
y = dict.fromkeys(keys,100)
print(y)

#딕셔너리 할당,복사
#할당 -> 실제로는 한개의 딕셔너리.
x = {'a':0, 'b':0, 'c':0, 'd':0}
y = x
if x is y :
    print('x: '+str(id(x)))
    print('y: '+str(id(y)))

x = {'a':0, 'b':0, 'c':0, 'd':0}
y = x.copy()
if x is not y :
    print('x: '+str(id(x)))
    print('y: '+str(id(y)))



# 출력
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items() :
    print(key, value)

# in 연산자
print('a' in x)

for key in x.keys() :
    print(key)

for value in x.values() :
    print(value)