def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add # 함수 자체 반환


c = calc() # 반환되 함수 keep

print(c(1), c(2), c(3))

'''
calc가 끝났는데도 c는 calc의 지역 변수 a, b를 사용해서 계산을 하고 있음
이렇게 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가,
함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저(closure)라고함. 
여기서는 c에 저장된 함수가 클로저
클로저를 사용하면 프로그램의 흐름을 변수에 저장할 수 있음.
특히 클로저는 내부 데이터를 숨기고 싶을 때 사용.
'''

# lambda closure
def calc():
    a = 3
    b = 5
    return lambda x : a * x + b

c = calc()
print(c(1), c(2), c(3))


# 클로저 : 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수
# 람다 : 익명 함수


# a * x + b의 결과를 함수 calc의 지역 변수 total에 누적
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add

c = calc()
c(1)
c(2)
c(3)


#호출횟수 카운트
def counter():
    count = 0
    def count_add():
        nonlocal count
        count += 1
        return count
    return count_add

c = counter()
#for i in range(10):
#    print(c(), end = ' ')



#호출횟수 카운트다운
def countdown(n):
    count = n + 1
    def count_deduct():
        nonlocal count
        count -= 1
        return count
    return count_deduct

n = int(input())
c = countdown(n)

for i in range(n):
    print(c(), end = ' ')

