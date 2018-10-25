# 클래스 데코레이터

class Trace:
    def __init__(self, func): # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func      # 호출할 함수를 속성 func에 저장

    def __call__(self):
        print(self.func.__name__, ' start')
        self.func()           # 속성 func에 저장된 함수를 호출
        print(self.func.__name__, ' end')

@Trace
def test():
    print('test.')

test()

def test():
    print('test.')

# @지정하지 않고 호출 가능
trace_test = Trace(test)  # 데코레이터에 호출할 함수를 넣어서 인스턴스 생성
trace_test()              # 인스턴스를 호출. __call__ 메서드가 호출됨



#매개변수와 반환값 처리 필요한 경우의 클래스 데코레이터

class Trace:
    def __init__(self, func):               # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func                    # 호출할 함수를 속성 func에 저장

    def __call__(self, *args, **kwargs):    # 호출할 함수의 매개변수를 처리
        r = self.func(*args, **kwargs)      # self.func에 매개변수를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        return r                             # self.func의 반환값을 반환

@Trace
def add(a, b):
    return a + b

add(10,3)

#매개변수가 있는 클래스 데코레이터
class Trace:
    def __init__(self, x):
        self.x = x

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            if r % self.x == 0:
                print('{0}(args={1}, kwargs={2})->{3}. {4}의 배수.'.format(func.__name__, args, kwargs, r, self.x))

            else:
                print('{0}(args={1}, kwargs={2})->{3}. {4}의 배수 아님.'.format(func.__name__, args, kwargs, r, self.x))
            return r
        return wrapper



@Trace(3)
def add(a, b):
    return a + b

print(add(9,3))