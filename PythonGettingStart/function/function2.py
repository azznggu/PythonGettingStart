# positional argument

tList = [10,20,30]
tTuple = ('a','b','c')


def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)

#print_numbers(*tList)

# list unpacking  -> 가변인수를 받는 경우 사용.

def print_args(*args):
    for arg in args:
        print(arg)

print_args(10)
print_args(10,20,30,40)
print_args(*tList)
print_args(*tTuple)


# 고정 인수 + 가변 인수
def print_num(a, *args):
    print(a)
    print(args)


print_num(1, 10, 20, 30)

print_num(1)

print_num(*[10,20,30]) # NG -  *args가 고정 매개변수보다 앞쪽에 오면 x
