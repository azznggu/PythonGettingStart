# 1-100
# 3: fizz
# 5: buzz
#mutual: fizzbuzz

for i in range(1,101):
    if (i%3 == 0) and (i%5 == 0):
        print("fizzbuzz")
    elif i%3 == 0 :
        print("fizz")
    elif i%5 == 0 :
        print("buzz")
    else :
        print(i)

for i in range(1,101):
    if i%15 == 0 :
        print("fizzbuzz")
    elif i%3 == 0 :
        print("fizz")
    elif i%5 == 0 :
        print("buzz")
    else :
        print(i)

# 단축코드
#문자열에 True를 곱하면 문자열이 그대로 나오고, 
#False를 곱하면 문자열이 출력되지 않는 특성 활용.(True는 1, False는 0으로 연산).
for i in range(1,101):
    print('fizz'*(i%3==0) + 'buzz'*(i%5==0) or i)