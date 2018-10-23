# 코루틴 바깥으로도 값 전달하기
'''
변수 = (yield 변수)
변수 = next(코루틴객체)
변수 = 코루틴객체.send(값)
'''

def sum_coroutine():
    total = 0
    while True:
        x = (yield total)
        total += x

co = sum_coroutine()
print(co.send(None))   # or   next(co) 로 코루틴 안의 yield까지 코드 실행(최초 실행)
print(co.send(1))
print(co.send(2))
print(co.send(3))

# yield를 사용하여 코루틴 바깥으로 값을 전달하면 next와 send의 반환값으로 받음
