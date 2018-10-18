#키워드 인수
def personal_info(name, age, address):
    print('이름: ',name)
    print('나이: ',age)
    print('이름: ',address)

personal_info(age=30, address='somewhere', name='park')


# print함수 키워드 인수 -> sep, end
print('a','b','c', sep=',', end='\n')


#dictionary 언패킹
x = {'name': 'park', 'age':30, 'address':'somewhere'}
personal_info(**x)


# * 두번쓰는 이유? 
# *-> 키만 출력 **->키,값 출력
personal_info(*x)


# 여러개 매개변수 받는 함수
def personal_info_multi(**kwargs):
    for kw, arg in kwargs.items():
        print(kw,': ', arg, sep='')

personal_info_multi(name='Jong')
personal_info_multi(name='Park', age=29)


# 여러개 매개변수 받는 함수 -> 특정 키 확인
def personal_info_condition(**kwargs):
    if 'name' in kwargs:  # in 으로 dictionary 안 특정 키 유무 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

personal_info_condition(name='park', age=29)


#고정 인수와 가변 인수(키워드 인수)를 함께 사용
def personal_info_mix(name, **kwargs):
    print(name)
    print(kwargs)

personal_info_mix('park')
personal_info_mix('park',age=99, address='somewhere')

#위치 인수 + 키워드 인수 사용 -> print 함수가 대표적.(위치인수로 출력할 값, 키워드인수로 sep, end등)
#순서는 args , kwargs 순이어야함.
def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1,2,3,4,5,sep='|', end='!')