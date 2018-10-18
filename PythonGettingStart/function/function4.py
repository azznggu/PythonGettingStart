# 매개변수 초기값 지정
# ex) print함수의 경우 키워드 인수 sep 초기값: ' '으로 지정되어있음.

def personal_info(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('Park',29)
personal_info('Park',29,'somewhere')

# 초기값 지정된 매개변수 뒤에 초기값 미지정 매개변수는 올 수 없음.
#def personal_info_error(name, age='비공개', address):
#    print('이름: ', name)
#    print('나이: ', age)
#    print('주소: ', address)


korean, english, mathematics, science = 55, 86, 81, 91

def get_max_score(*args):
    temp = 0
    for i in args:
        if i > temp:
            temp = i
    return temp

max = get_max_score(korean, english, mathematics, science)
print(max)

# args -> 리스트 -> max함수 사용으로 더 간단히 코딩 가능.
def get_max(*args):
    return max(args)

#최소
def get_min(*args):
    return min(args)

#평균
def get_avr(*args):
    return sum(args)/len(args)

print(get_avr(10,20,30,40))
