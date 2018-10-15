# list안 for, if문 사용 가능.

a = [i for i in range(10)]
print(a)

b = list(i for i in range(10))
print(b)

#요소를 다른값과 연산 가능.
c = list(i*2 for i in range(10))
print(c)

#반복문 뒤 조건문 지정.
#range에의해 생성된 숫자 요소 조건문(짝수)인 경우에만 i로 지정, i를 리스트 요소로 리스트 생성.
d = list(i for i in range(10) if i%2== 0)
print(d)


#for,if 복수 사용 가능.
e = list(i*j for i in range(1,10) 
             for j in range(1,10))
print(e)