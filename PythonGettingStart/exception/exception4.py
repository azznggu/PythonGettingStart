'''
예외 만들기

class 예외이름(Exception):
    def __init__(self):
        super().__init__(에러메시지)
'''

class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

def three_multiple():
    try:
        x = int(input('3의 배수 입력: '))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e :
        print('예외 발생.', e)

three_multiple()

