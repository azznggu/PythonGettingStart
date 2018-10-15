#   python2.7 -> range(num) -> list생성, 큰 숫자 지정시 메모리 사용 up -> xrange사용
#   python3 -> range객체 생성
#for i in range(10):
#    print('print!')

# range범위 지정(끝나는 숫자는 생성된 숫자에 포함되지 않음))
#for i in range(5,10):
#    print('print'+str(i)) # 5~9출력

#증가폭 지정
#for i in range(1,10,2):
#    print('print'+str(i)) # 1,3,5,7,9

#감소
#for i in range(10,0,-1):
#    print('print'+str(i))

#역순
#for i in reversed(range(1,20,3)) :
#    print('print'+str(i))


#while
num = int(input("enter loop number: "))
while num <= 100:
    num += 1
    if num % 2 != 0:
        continue
    else :
        print(num)

