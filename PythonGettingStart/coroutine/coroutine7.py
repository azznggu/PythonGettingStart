def calc():
    result = 0
    while True:
        ex = (yield result)
        cal = ex.split()
        if cal[1] == '+':
            result = int(cal[0])+int(cal[2])
        elif cal[1] == '-':
            result = int(cal[0])-int(cal[2])
        elif cal[1] == '*':
            result = int(cal[0])*int(cal[2])
        elif cal[1] == '/':
            result = int(cal[0])/int(cal[2])

expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()