# python 내장 함수 iter , next
#iter(iterable)
#iter는 반복 가능한 객체에서 이터레이터를 반환하고(객체의 __iter__ 호출), 
#next는 이터레이터에서 값을 차례대로 꺼냅니다(객체의 __next__ 호출)

it = iter(range(3))  # == range(3).__iter__()
#print(next(it))     # == range(3).__iter__().__next__()
#print(next(it))
#print(next(it))

#iter -> 반복을 끝낼값 지정 가능. 반복 가능한 객체(iterable) 대신 호출 가능한 객체(callable)를 넣어줌.
#        반복을 끝낼값을 sentinel(감시병) 라고 함. 반복을 감시하다가 특정 값이 나오면 반복을 끝낸다고 해서 sentinel

#iter(callable, sentinel)

# random으로 무작위 값 생성하다가 특정값 나오면 반복을 끝내도록 만들 수 있음
#호출 가능한 객체를 넣어야 하므로 매개변수가 없는 함수 또는 람다 표현식
import random
it = iter(lambda: random.randint(0,5), 2)
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))

#for문
#for i in iter(lambda: random.randint(0,5), 2):
    #print(i, end=' ')

#iter 함수를 활용하면 if 조건문으로 매번 숫자가 2인지 검사하지 않아도 되므로 코드가 좀더 간단해집니다
#아래 코드 동작과 동일.
while True:
    i = random.randint(0,5)
    if i == 2:
        break
    #print(i, end=' ')

#next -> 기본값 지정 가능. 지정 시 반복이 끝나도 stopiteration 발생하지 않고 기본값 출력.
#for i in iter(range(10)):
it = iter(range(3))
print(next(it, 'a'))
print(next(it, 'a'))
print(next(it, 'a'))
print(next(it, 'a'))