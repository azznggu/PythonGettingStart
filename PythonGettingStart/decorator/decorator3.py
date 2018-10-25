# 매개변수가 있는 데코레이터

def is_multiple(x):
    def real_deco(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % x != 0:
                print('{0}의 반환값:{1} -> {2}의 배수가 아닙니다.'.format(func.__name__,r,x))
            else:
                print('{0}의 반환값:{1} -> {2}의 배수입니다.'.format(func.__name__,r,x))
            return r
        return wrapper
    return real_deco

@is_multiple(3)
def add(a, b):
    return a + b

print(add(10,20))
print(add(10,22))



# 데코레이터 여러개 사용 -> 원래 함수 이름 출력 안될 경우
# functools - wraps 데코레이터 이용.
# @functools.wraps는 원래 함수의 정보를 유지시켜줍니다. 
# 따라서 디버깅을 할 때 유용하므로 데코레이터를 만들 때는 
# @functools.wraps를 사용하는 것이 좋습니다.
    
import functools

def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % 3 == 0:
                print('{0} result: {1}  -> {2}의 배수'.format(func.__name__, r, x))
            else:
                print('{0} result: {1}  -> {2}의 배수 아님.'.format(func.__name__, r, x))
            return r
        return wrapper
    return real_decorator

@is_multiple(5)
def add(a, b):
    return a + b

add(1, 7)
