


#ex)
def outer(message):

    def inner():
        print(message)

    return inner

closure = outer("hello!")
closure()


#global
x = 10
def foo():
    print(x)

foo()
print(x)


#local
def foo():
    y = 10
    print(y)

foo()
#print(y) #-> local변수 y엔 접근불가.



x = 10 #전역변수 x
def foo():
    global x #전역변수 사용 선언.
    x = 20
    print(x)

foo()
print(x)

#기존 전역변수 선언 없는 경우
def foo():
    global z # z를 전역변수로 선언
    z = 30
    print(z)

foo()
print(z)

#네임스페이스
#파이썬에서 변수는 네임스페이스(namespace, 이름공간)에 저장. 
#locals 함수를 사용하면 현재 네임스페이스를 딕셔너리 형태로 출력.
#print(locals())


def foo():
    x = 10
    print(locals())
foo() #-> 지역 범위 네임스페이스를 출력하므로 'x:10'만 들어있음.