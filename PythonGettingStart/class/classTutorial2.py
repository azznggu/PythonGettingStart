#클래스 속성
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다'.format(self.hello, self.name))

park = Person('Park', 29, 'kawasaki')
park.greeting()

print(park.name)
print(park.age)
print(park.address)



# __method__ -> 매직 메서드, 스페셜 메서드. 파이썬이 자동으로 호출해주는 메서드.
# self -> 인스턴스 자기자신


#클래스 위치인수, 키워드 인수
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

park = Person(*['park',29,'miyazakidai'])
print(park)

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

park = Person(**{'name':'park', 'age':29, 'address':'kawasaki'})
print(park)




#인스턴스 생성 후 속성 추가 -> 추가한 속성은 해당 인스턴스에만 생성
class Person :
    pass

maria = Person()
maria.name = 'maria'
print(maria.name)

#특정 속성만 허용할 경우 -> __slots__에 허용할 속성 리스트 작성
class Person :
    __slots__ = ['name', 'age', 'address']

park = Person()
#park.hobby ='none' -> AttributeError("'Person' object has no attribute 'hobby'",)

