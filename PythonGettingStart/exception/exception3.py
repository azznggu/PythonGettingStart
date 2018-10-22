# 예외 발생시키기

#try:
#     x = int(input('3의 배수 입력: '))
#     if x % 3 != 0:
#         raise Exception('3의 배수가 아닙니다.')
#     print(x)
#except Exception as e: # raise exception 시 기재한 에러 메시지 -> e
#    print('예외 발생.', e)


#호출한 함수 내부 raise -> exception처리 없는 경우 상위 코드 블록에서 처리.

#def three_multiple():
#    x = int(input('3의 배수 입력: '))
#    if x % 3 != 0:
#        raise Exception('3의 배수가 아닙니다.')
#    print(x)


#try:
#    three_multiple()
#except Exception as e: # raise exception 시 기재한 에러 메시지 -> e
#    print('예외 발생.', e)

#three_multiple()

#함수 내부에서 처리한 예외 -> 상위 코드 블록에서 재처리
def three_multiple():
    try:
        x = int(input('3의 배수 입력: '))
        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        #raise
        raise Exception('3의 배수가 아닙니다.2') #raise -> except에서 상위 블록으로 raise시 다른 예외 발생시키기 가능.
                                                                

try:
    three_multiple()
except Exception as e:
    print('스크립트 파일에서 예외 발생.', e)



# assert 이용한 예외처리. 지정된 조건식이 거짓일경우 AssertionException발생시킴.
# assert-> 디버그 모드 시에만 실행, 파이썬은 기본적으로 디버깅 모드(__debug__= True)이므로 
# assert실행안하려면  python -O옵션으로 실행. (python -O 스크립트파일.py)

x = int(input('3의 배수 입력: '))
assert x % 3 == 0, '3의 배수가 아닙니다.'
print(x)