tList = ['a',10, 2.3, True]
print(tList)

# 빈 리스트 생성
a = []
b =list()

#range활용한 리스트 생성
rangedList = list(range(10))
print(rangedList)

rangedList = list(range(10,0,-1))
print(rangedList)

rangedList = list(range(10,20,2))
print(rangedList)

#문자열 list화
text = 'test string'
textList = list(text)
print(textList)

#list요소 접근 - 인덱스

a = [30, 55, 60, 1, 0]
print(a)
print(a[3])
print(a[-2])

#요소 할당
b = [0, 0, 0, 0, 0]
b[0] = 1
b[1] = 3
b[2] = 13
b[3] = 23
b[4] = 33
print(b)

#리스트 길이
print(str(len(b)))

#리스트 슬라이스
a = [0, 10, 20, 30, 40, 50, 60]
print(a[0:3])
print(a[0:7])

#시작 인덱스와 끝 인덱스를 같은 숫자로 지정하면 아무것도 가져오지 않습니다. 
#a[1:2]처럼 끝 인덱스를 1이 더 크게 지정해야 요소 하나를 가져옵니다.

print(a[1:1])
print(a[1:2])
print(a[1:-1])
print(a[:3])
print(a[4:])
print(a[:])



