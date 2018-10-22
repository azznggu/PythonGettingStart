def binary(num):
    #b = list('{0:b}'.format(num))
    b = bin(num).lstrip('0b')
    print(b)
    gap = 0
    temp = 0
    for i in range(len(b)):
        if b[i] == '0':
            gap += 1
        else : # 1
            if temp < gap:
                temp = gap
            gap = 0
    return temp

print(binary(74901729))




            