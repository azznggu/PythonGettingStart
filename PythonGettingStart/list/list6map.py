# map -> 리스트 요소를 지정 함수로 처리
# list(map(함수, 리스트)

a = [1.2, 2.5, 3.3, 4.3]
def mappingToInt(list):
    for i in range(len(a)):
        a[i] = int(a[i])
    print(a)

#mappingToInt(a)

#map활용
a = [1.2, 2.5, 3.3, 4.3]
a = list(map(int, a))
#print(a)

def inputList():
    a = map(int, input().split())
    iList = list(a)
    print(iList)

inputList()