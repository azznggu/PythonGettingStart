#코루틴에 값 보내기 (yield 사용)

def number_coroutine():
    while True:      # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = yield    # 코루틴 바깥에서 값을 받아옴
        print(x)

co = number_coroutine()
next(co)             # 코루틴 안의 yield까지 코드 실행(최초 실행)

# 코루틴에 값을 보냄
co.send(1)
co.send(2)
co.send(3)



#send로 코루틴의 코드를 최초로 실행하기
# 코루틴의 코드를 최초로 실행할 때 next 함수(__next__ 메서드)를 사용했지만, 
# 코루틴객체.send(None)과 같이 send 메서드에 None을 지정해도 코루틴의 코드를 최초로 실행할 수 있습니다.
# next 실행 데코레이터를 만들어서 @로 호출하여 사용가능.
