#2차원 리스트
a = [[1,1],[2,2],[3,3]]

#2차원 튜플
b = ((1,1),(2,2),(3,3))

#리스트, 튜플 혼합
c = [(1,1),(2,2),(3,3)]



def printDList(list):
    for x,y in list:
        print(x,y)

def printDElement(list):
    for i in list:
        for j in i:
            print(j, end='')
        print()

sampleList = [[10,20],[30,40],[50,60]]

def printDElement2(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j])
        print()


def while1(list):
    i = 0
    while i < len(list):
        x,y = list[i]
        print(x,y)
        i += 1

def while2(list):
    i=0
    while i < len(list):
        j = 0
        while j < len(list[i]):
            print(list[i][j], end=' ')
            j+=1
        i+=1
        print()
    
def initDimList1(outer,inner):
    a = []
    for i in range(outer):
        b = []
        for j in range(inner):
            b.append(0)
        a.append(b)
    return a

def initDimList2(outer,inner):
    a = [[0 for j in range(inner)] for i in range(outer)]
    return a
#printDList(a)
#printDElement(a)
#printDElement2(sampleList)
#while1(sampleList)
#while2(sampleList)

print(initDimList2(5,4))