# 리스트 최대, 최소갑 요소 구하기

a = [10, 55, 30, 2, 14]

#1. loop,if
def minInList(list):
    smallest = a[0]
    for i in a :
        if i < smallest:
            smallest = i
    print(smallest)

def maxInList(list):
    largest = a[0]
    for i in a :
        if i > largest:
            largest = i
    print(largest)

minInList(a)
maxInList(a)


#2. sort, reverse활용
a = [10,2,55,35,1]

a.sort()
print(a[0])

a.sort(reverse=True)
print(a[0])


#3. 내장 함수 min, max 사용
print(min(a))
print(max(a))



# 요소 합계

a = [1,2,4,16]
#1. for
def sumListElement(list):
    sum = 0
    for i in list:
        sum+=i
    print(sum)

sumListElement(a)
#2. 내장함수 sum
print(sum(a))