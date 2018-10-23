#하위 코루틴 반환값 가져오기

#generator에서 yield from -> 바깥으로 값을 여러번 전달
#yield from coroutine -> 해당 coroutine에서 return으로 반환되는 값을 가져옴
# var = yield from coroutine()


def accumulate():
    total = 0
    while True:
        x = (yield)      #코루틴 밖에서 값을 가져옴
        if x is None:    #가져온 값이 None이면
            #return total #total 반환    # 코루틴도 제네레이터이므로 return 시 StopIteration 발생.
            raise StopIteration(total)   # 따라서 raise로 예외를 직접 발생 및 값 지정 시 yield from으로 반환가능.
        total += x

def sum_coroutine():
    while True:
        total = yield from accumulate() #accumulate의 반환값 가져옴
        print(total)

co = sum_coroutine()
next(co)

for i in range(11):
    co.send(i)
co.send(None)

for i in range(101):
    co.send(i)
co.send(None)



#코루틴에서 yield에 값을 지정해서 바깥으로 전달했다면 yield from은 해당 값을 다시 바깥으로 전달

def number_coroutine():
    x = None
    while True:
        x = (yield x) # 코루틴 바깥에서 값을 받아오면서 바깥으로 값 전달
        if x == 3:
            return x

def print_coroutine():
    while True:
        x = yield from number_coroutine() # 하위 코루틴의 yield에 지정된 값을 다시 바깥으로 전달
        print('print_coroutine: ', x)

co = print_coroutine()
next(co)

x = co.send(1)
print(x)
x = co.send(2)
print(x)
co.send(3)

