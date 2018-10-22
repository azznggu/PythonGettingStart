'''
yield -> 한번씩 바깥에 값 전달
yield from -> 여러번 바깥에 값 전달
yield from은 파이썬 3.3 이상부터 사용 가능

  yield from 반복가능한객체(iterable)
  yield from 이터레이터
  yield from 제네레이터객체
'''

def num_generator():
    x = [1,2,3]
    for i in x:
        yield i

#for i in num_generator():
   #print(i)

#yield from 반복가능한객체(iterable)
def multi_num_generator(list):
    yield from list

#for i in multi_num_generator(range(10)):
#    print(i)

g = multi_num_generator([1,2,3])

#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))


#yield from 제네레이터객체

def num_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def multi_num_generator(x):
    yield from x

for i in multi_num_generator(num_generator(3)):
    print(i)


# 제네레이터 표현식
#리스트 표현식을 사용할 때 [ ](대괄호)를 사용했습니다. 같은 리스트 표현식을 ( )(괄호)로 묶으면 제네레이터 표현식이 됩니다. 
#리스트 표현식은 처음부터 리스트의 요소를 만들어내지만 제네레이터 표현식은 필요할 때 요소를 만들어내므로 
#성능이 더 좋고 메모리를 절약할 수 있습니다.
#ex)
list = [i for i in range(30) if i % 5 == 0]
print(list)
gen = (i for i in range(30) if i % 5 == 0)
for i in gen:
    print(i, end=' ')







