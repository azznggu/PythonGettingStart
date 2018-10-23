def add(a,b):
    c = a + b
    print(c)
    print('add function')

def calc():
    add(1,2)
    print('calc function')

calc()

# calc -> main routine   add -> sub routine  (종속 관계)

# 코루틴(coroutine) - 서로 협력하는 루틴 (대등 관계), 특정 시점에서 상대방 코드 실행. 제네레이터의 특별한 형태.
#코루틴은 함수가 종료되지 않은 상태에서 메인 루틴의 코드를 실행한 뒤 다시 돌아와서 코루틴의 코드를 실행합니다. 
#따라서 코루틴이 종료되지 않았으므로 코루틴의 내용도 계속 유지됩니다.
#일반 함수는 호출을 하면 코드를 한 번만 실행할 수 있지만, 코루틴은 코드를 여러 번 실행할 수 있습니다. 
#참고로 함수의 코드를 실행하는 지점을 진입점(entry point)이라고 하는데 코루틴은 진입점이 여러 개인 함수입니다.


#코루틴은 부분적으로, 그리고 특정한 상황이 맞아 떨어졌을 때 실행되는 함수로써,
#그 작업이 완료가 되기전까지, 미래의 어느시점에 재개될 수 있다.

# 스레드와 코루틴은 다름(코루틴은 비동기 x)
# 멀티 스레드 코드 작성 시 -> 스레드간 교착, 경합 상태 등으로 인해 버그 발생률도 높아짐.
# 코루틴 -> 단일 스레드에서 멀티 태스킹 처리
# 함수가 호출되서 끝나는 서브루틴의 개념과 달리 yield return 을 사용함으로써 그 위치를 기억하고 
# 다음 호출 때 그곳부터 다음을 실행 할 수있도록 하는 것이다. 
# 그래서 여러개의 코루틴을 동작시키고 각기다른 시점에 yield가 반환되도록 한다면 
# 마치 어러개의 쓰래드가 동시에 동작하는것과 같은 효과가 나타난다