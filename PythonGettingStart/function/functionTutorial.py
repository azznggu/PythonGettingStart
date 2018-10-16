#doc string
def add(a, b):
    """
    add function. return a + b.
    param a : int
    param b : int
    """
    return a + b

print(add(10,20))

# doc string 확인
help(add)


#여러 개 값 반환 -> return 객체 수가 여럿 -> 실제로는 튜플로 반환됨(언패킹 특성)
def add_sub(a, b):
    return a+b, a-b

x, y = add_sub(10,5)
print(x,y)