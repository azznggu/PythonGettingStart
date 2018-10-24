#  매개변수와 반환값을 처리하는 데코레이터 만들기

def trace(func):         #호출할 함수를 매개변수로 받음
    def wrapper(a, b):   #호출할 함수의 매개변수를 똑같이 지정
        r = func(a, b)   #func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r         # func의 반환값을 반환
    return wrapper       # wrapper 함수 반환

@trace
def add(a, b):
    return a + b

print(add(a=10,b=20))




# 매개변수 고정되지 않은 경우(가변인수함수)에 대한 데코레이터

def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
        return r
    return wrapper

@trace
def get_max(*args):          #*args -> tuple(iterable)
    return max(args)

@trace
def get_min(**kwargs):        #**kwargs -> dict(iterable)
    return min(kwargs.values())

print(get_max(1,2,4,99,100,21,3))
print(get_min(a=1,b=10,c=2,d=5))




#클래스를 만들면서 메서드에 데코레이터를 지정할 때는 self를 주의
#인스턴스 메서드는 항상 self를 받으므로 
#데코레이터를 만들 때도 wrapper 함수의 첫 번째 매개변수는 self로 지정해줍니다(클래스 메서드는 cls). 
#마찬가지로 func을 호출할 때도 self와 매개변수를 그대로 넣어줍니다.
def trace(func):
    def wrapper(self, a, b):
        r = func(self, a, b)
        print('{0}({1}+{2}) -> {3}'.format(func.__name__, a, b, r))
        return r
    return wrapper


class Calc:
    @trace
    def add(self, a, b):
        return a + b

c = Calc()
print(c.add(10,20))




