'''
데코레이터 - 장식하다?
@로 시작하는 것들이 데코레이터
ex) @staticmethod, @classmethod, @abstractmethod 
함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용
'''

# ex) 함수의 시작, 끝 출력(print)가 반복되지않도록, 데코레이터 작성하여 사용
def trace(func):
    def wrapper():
        print(func.__name__, 'start')
        func()
        print(func.__name__, 'end')
    return wrapper

def hello():
    print('hello')

def bye():
    print('bye')

trace_hello = trace(hello)
trace_bye = trace(bye)
trace_hello()
trace_bye()


# @를 사용하여, 호출할 함수에 데코레이터 지정 가능
@trace
def test():
    print('decorator set test')
test()


#데코레이터 복수 지정 -> 여러 줄로 복수의 데코레이터 지정 가능. 데코레이터가 실행되는 순서는 위에서 아래 순

def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper

@decorator1
@decorator2
def hi():
    print('hi')
hi()


# @미사용시의 동작
decorated_multi = decorator1(decorator2(hi))
decorated_multi()
