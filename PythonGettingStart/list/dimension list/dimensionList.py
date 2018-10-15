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



#printDList(a)
#printDElement(a)
#printDElement2(sampleList)
