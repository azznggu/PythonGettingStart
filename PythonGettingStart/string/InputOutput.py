#input
#input = input("input sth:")
#print(input)

#숫자의 경우 변환필요.
def inputTwo() :
    first = int(input("enter 1st:"))
    second = int(input("enter 2nd:"))
    print(first+second)

#split사용으로 복수 문자 입력 받기 가능.
def inputThree():
    a,b,c = input("enter three: ").split()
    print(a)
    print(b)
    print(c)

#map함수를 활용, int함수를 input결과값에 할당
def inputThreeByMap():
    a,b,c = map(int, input("enter three int: ").split())
    print(a+b+c)

#print함수 -> seperator지정
def printWithSeperator():
    print('a','b','c',sep=' . ')

def printEnd():
    print('aa',end='')
    print('bb',end='')
    print('cc',end='')

def printLine():
    print('a','b','c',sep='\n')
    
printLine()
print('1\n2\n3')
printEnd()

#제어문자
#₩n: 다음 줄로 이동하며 개행이라고도 부릅니다.
#₩t: 탭 문자, 키보드의 Tab 키와 같으며 여러 칸을 띄웁니다.
#₩₩: ₩ 문자 자체를 출력할 때는 ₩를 두 번 써야 합니다.


