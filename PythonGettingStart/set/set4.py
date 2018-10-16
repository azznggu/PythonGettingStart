a = {'a', 'b', 'c', 'd'}
for i in a :
    print(i)

print('a' in a)

#set expression statement
a = set(i for i in 'apple')
print(a)
a = {i for i in 'apple'}
print(a)


a = set(i for i in 'pineapple' if i not in 'le')
print(a)



#공배수구하기 (교집합)
a = {i for i in range(1,101) if i%3 == 0}
b = {i for i in range(1,101) if i%5 == 0}

print(a&b)
