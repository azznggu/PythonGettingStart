# lambda & map 사용

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x : str(x) if x % 3 == 0 else x

#r_list = list(map(f,a))
#print(r_list)


#람다 표현식 안에서 조건부 표현식 if, else를 사용할 때는 :(콜론) x
#조건부 표현식은 식1 if 조건식 else 식2 형식으로 사용
#식1은 조건식이 참일 때, 식2는 조건식이 거짓일 때 사용
#if else는 항상 같이 사용되어야.
#elif는 사용불가.

f_2 = lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10
print(list(map(f_2, a)))


#map: iterator에 함수 적용한 iterator 생성. 여러개 iterator 매개변수도 가능.
a = [1,2,3,4,5]
b = [2,4,6,8,10]
m_list = list(map(lambda x, y : x*y,a,b))
print(m_list)


#filter:특정'조건'에 맞는 요소만 반환.
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
f_list = list(filter(lambda x : x > 5 and x < 10, a))
print(f_list)


#reduce:처음요소부터 순차적으로 지정 함수 처리. (줄여나간다?는 느낌)
#reduce->파이썬 3부터 내장 함수 x. 
from functools import reduce
a = [1,2,3,4,5]
print(reduce(lambda x,y : x + y, a))


#람다 대신 리스트(딕셔너리, 튜플)표현식 사용 가능한 경우->표현식으로 처리(해석, 속도면에서 나음)
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
f_list = [i for i in a if i>5 and i<10]
print(f_list)


# for, while 처리 가능한 경우 reduce대신 loop문 사용(python3 내장함수에서 제외된 이유..)
a = [1,2,3,4,5]
x = a[0]
for i in range(len(a)-1):
    x += a[i+1]
print(x)


#practice - list에서 특정 파일 형식 해당 요소 추출.
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
f_list = list(filter(lambda x : x.find('.jpg') != -1 or x.find('.png') != -1, files))
print(f_list)



files = input().split()
e_list = list(map(lambda x: str(x).zfill(7),files)) 
e_list = list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]),x.split('.')[1]), files))
print(e_list)
