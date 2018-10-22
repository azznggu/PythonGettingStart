# generator 만들기

def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

for i in number_generator(5):
    print(i)


# generator사용, yield에서 함수 호출
def upper_generator(x):
    for i in x:
        yield i.upper()

x = ['apple', 'banana', 'orange']

for i in upper_generator(x):
    print(i, end=' ')
