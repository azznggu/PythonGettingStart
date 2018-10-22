'''
generator : iterator를 생성해주는 함수
    iterator - __iter__ , __next__, __getitem__ 메서드 구현 필요.
    generator -  함수 안에서 yield 키워드만 사용. iterator보다 간단히 작성 가능.
    
    함수 안에서 yield 키워드 사용 시 함수는 generator가 되며, yield에는 값(변수) 지정
    generator 객체에서 __next__메서드 호출때마다 yield 값을 발생시킴
    generator 함수의 객체 = iterator
'''

def number_generator():
    yield 0
    yield 1
    yield 2

for i in number_generator():
    print(i)

# generator함수로 만든 객체가 iterator인지 확인
g = number_generator()
print(dir(g)) # -> 객체에 __iter__, __next__ 메서드가 있음을 확인.

# iterator와 차이점
# 1.이터레이터는 __next__ 메서드 안에서 직접 return으로 값을 반환했지만 
#   제네레이터는 yield에 지정한 값이 __next__ 메서드(next 함수)의 반환값으로 나옴
# 2.이터레이터는 raise로 StopIteration 예외를 직접 발생시켰지만 
#   제네레이터는 함수 끝까지 도달하면 StopIteration 예외가 자동으로 발생



for i in number_generator(): # number_generator()->__iter__() -> __next__() -> yield 값을 발생
    print(i)



# yield 키워드는 왜 generate가아니라 yield?
# -> yield : 생산하다, 양보하다 -> yield 사용 시 값을 함수 밖으로 전달하면서 코드 실행을 함수 밖으로 양보.
#                                  현재 함수를 잠시 중단하고 함수 바깥 코드가 실행되도록 만듦.


def number_generator():
    yield 0
    yield 1
    yield 2

g = number_generator()

a = next(g)
print(a)

b = next(g)
print(b)

print('take a rest.')

c = next(g)
print(c)

#제네레이터는 함수를 끝내지 않은 상태에서 yield를 사용하여 값을 바깥으로 전달할 수 있습니다. 
#즉, return은 반환 즉시 함수가 끝나지만 yield는 잠시 함수 바깥의 코드가 실행되도록 양보하여 값을 가져가게 한 뒤 
#다시 제네레이터 안의 코드를 계속 실행하는 방식입니다.


#제네레이터와 return
#제네레이터는 함수 끝까지 도달하면 StopIteration 예외가 발생합니다. 
#마찬가지로 return도 함수를 끝내므로 return을 사용해서 함수 중간에 빠져나오면 StopIteration 예외가 발생합니다.
#특히 제네레이터 안에서 return에 반환값을 지정하면 StopIteration 예외의 에러 메시지로 들어갑니다.

def one_generator():
    yield 1
    return 'return'


try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)