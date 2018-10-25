# html 태그 데코레이터 작성
def html_tag(arg):  #데코레이터 자체 매개변수 arg
    def real_decorator(func):  
        def wrapper(): #func -> 매개변수 없으므로 wrapper도 없음.
            content = func()
            result = '<{0}>{1}</{2}>'.format(arg, content, arg)
            return result
        return wrapper
    return real_decorator




a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())