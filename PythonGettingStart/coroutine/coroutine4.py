#  코루틴 종료, 예외 처리
def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')

co= number_coroutine()
next(co)
for i in range(20):
    co.send(i)

co.close() # 코루틴 종료
print()
#사실 파이썬 스크립트가 끝나면 코루틴도 끝나기 때문에 close를 사용하지 않은 것과 별 차이가 없습니다. 
#하지만 close는 코루틴의 종료 시점을 알아야 할 때 사용하면 편리합니다.


#루틴 객체에서 close 메서드를 호출하면 코루틴이 종료될 때 GeneratorExit 예외가 발생합니다. 
#따라서 이 예외를 처리하면 코루틴의 종료 시점을 알 수 있습니다.
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit as e:
        print(' 코루틴 종료.')

co= number_coroutine()
next(co)
for i in range(20):
    co.send(i)

co.close() # 코루틴 종료



#코루틴 안에 특정 예외 발생시키기
def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total   #코루틴 밖으로 값 전달

co = sum_coroutine()
next(co)
for i in range(20):
    co.send(i)

#코루틴 안의 except에서 yield를 사용하여 바깥으로 전달한 값은 throw 메서드의 반환값으로 나옵니다
result = co.throw(RuntimeError, '예외로 루틴 끝내기')
print(result)
