'''
else, finally
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드
'''

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10/x
except ZeroDivisionError as e:
    print('숫자를 0으로 나눌 수 없습니다.')
else:
    print(y)
finally:
    print('코드 실행이 끝났습니다.')
print(x)

#예외처리문 안에서 선언한 변수 -> 함수가 아니므로 스택 프레임 생성x
# 따라서 변수를 만들더라도 try 바깥에서 사용가능.
