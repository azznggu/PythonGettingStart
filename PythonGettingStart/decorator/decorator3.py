# 매개변수가 있는 데코레이터

def is_multiple(x):
    def real_deco(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % x != 0:
                print('result:{0} -> {1}의 배수가 아닙니다.'.format(r,x))
            else:
                print('result:{0} -> {1}의 배수입니다.'.format(r,x))
            return r
        return wrapper
    return real_deco

@is_multiple(3)
def add(a, b):
    return a + b

print(add(10,20))
print(add(10,22))
