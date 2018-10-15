#리스트를 다른 변수에 할당하면 리스트는 두 개가 될 것 같지만 실제로는 리스트가 한 개
a = [0,0,0,0,0]
b = a
b[2] = 99
print("a id: "+str(id(a)))
print(a)
print("b id: "+str(id(b)))
print(b)

#복사하려면 copy사용
c = a.copy()
c[2] = 100
print("a id: "+str(id(a)))
print(a)
print("c id: "+str(id(c)))
print(c)


a = [10,20,30,40,50]
for i in range(len(a)) :
    print(a[i])

#for에서 인덱스와 요소의 값을 동시에 출력하기
#-> enumerate를 사용

for index, value in enumerate(a):
    print(index, value)