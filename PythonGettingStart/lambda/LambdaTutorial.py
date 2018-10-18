#lambda - 식 형태 함수 작성(한줄) -> 다른 함수 인수로 넣을 때 등 사용.
#익명 함수(anonymous function)로 불리기도.

#before
def plus_ten(x):
    return x + 10

result_before = list(map(plus_ten, [1,2,3]))
print(result_before)


#after
result_after = list(map(lambda x : x + 10, [1,2,3]))
print(result_after)       


#함수로 동작하지만, 할당도 가능.
f = lambda x : x + 10
result_assigned = list(map(f,[10,20,30]))
print(result_assigned)

#식 자체로 호출하는 경우 뒤에 괄호 사용, 뒤에 인수
print((lambda x : x + 10)(10))

#람다 표현식 안에서는 새 변수 선언 불가. 그런 경우엔 def로 작성해야..
#print((lambda x: y + 10)(10)) -> y not defined
#단, 바깥에서 선언한 변수의 경우 사용 가능.
y = 10
print((lambda x: y + 10)(10))


#람다로 매개변수 없는 함수 작성 시 , lambda 뒤에 아무것도 선언 x, : 만 붙이기
print((lambda : 10*20)())
print((lambda : y*20)())