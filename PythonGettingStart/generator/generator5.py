def prime_number_generator(start, stop):
    #yield from [i for i in range(start, stop) if i % i == 0 & i % 1 == 0]
    for i in range(start, stop):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            yield i



start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
