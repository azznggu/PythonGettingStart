#index
a = (1, 3, 3, 40, 50, 100)
print(a.index(40))
#count
print(a.count(3))
# + , *
a = (1,2,3)
b = (4,5,6)
c = a + b
print(c)

d = a+b*2
print(d)

# for, if
a = tuple(i for i in range(10) if i%2 ==0)
print(a)

# map
a = (1.2, 2.3, 4.7, 5.25)
a = tuple(map(int, a))
print(a)

#max min sum
print(max(a))
print(min(a))
print(sum(a))