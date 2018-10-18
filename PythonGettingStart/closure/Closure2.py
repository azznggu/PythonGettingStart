def print_hello():
    hello ="hi!"

    def print_message():
        print(hello)
    print_message()

print_hello()


def calc():
    total = 0 # calc의 지역변수
    print(locals())

    def add(a,b):
        print(locals())
        #total = total + a + b -> add의 지역변수 total이 할당되기 전에 참조하려고해서 에러 발생 UnboundLocalError: local variable 'total' referenced before assignment
        #겉으로 보기에는 함수 calc의 지역 변수 total에 접근한 것 같지만 
        #실제로는 함수 add 안에서 이름이 같은 지역 변수 total 사용하려다가 에러가 발생.
        #파이썬에서는 함수 안에서 변수를 만들면 항상 현재 함수의 지역 변수가 됨.
    add(10,20)
    add(30,40)
    print(total)
#calc()


#함수 바깥에 있는 지역 변수의 값을 변경하려면 nonlocal 키워드를 사용
#nonlocal은 함수 바깥의 지역 변수를 찾을 때 가까운 함수부터 먼저 찾음
def calc():
    total = 0 # calc의 지역변수
    print(locals())

    def add(a,b):
        nonlocal total
        print(locals())
        total = total + a + b
    add(10,20)
    add(30,40)
    print(total)

calc()

#매개변수도 함수 안에서만 사용할 수 있는 지역 변수이므로 nonlocal을 사용가능
def calc(total):
    print(locals())
    def add(a,b):
        nonlocal total
        print(locals())
        total = total + a + b
    add(10,20)
calc(0)

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
A()


#파이썬에서 global을 제공하지만 함수에서 값을 주고받을 때는 매개변수와 반환값을 사용하는 것이 좋음
#특히 전역 변수는 코드가 복잡해졌을 때 변수의 값을 어디서 바꾸는지 알기가 힘듦
#따라서 전역 변수는 가급적이면 사용하지 않는 것을 권장