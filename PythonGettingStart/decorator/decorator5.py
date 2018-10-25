def type_check(x, y):
    def real_decorator(func):
        def wrapper(a, b):
            if not (isinstance(a, x) and isinstance(b, y)):
                raise RuntimeError('자료형이 다릅니다.')
            return func(a, b)
        return wrapper
    return real_decorator

@type_check(int, int)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add('hello', 'world'))