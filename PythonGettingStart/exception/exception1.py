'''
try except
예외가 발생했을 때도 스크립트 실행을 중단하지 않고 계속 실행하게 해주는 예외처리
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
'''

try:
    x = int(input("10을 나눌 숫자: "))
    y = 10/x
    print(y)
except:
    print("예외 발생.")


# 특정 예외 처리, as e -> 예외 메시지 정보
y = [10, 20, 30]
print(y)
try:
    index, x = map(int, input('인덱스와 나눌 숫자 입력: ' ).split(' '))
    print(y[index]/x)

except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.', e)
except IndexError as e:
    print('잘못된 인덱스.', e)
except ValueError as e:
    print('입력 항목 부족.', e)
