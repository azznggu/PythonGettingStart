class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag("book")

maria = Person()
maria.put_bag("pen")

print(james.bag) # -> 확인해보면 james와 maria의 bag인스턴스가 공유되어있음..

print(Person.bag) # -> 생성한 인스턴스의 속성이 아닌 클래스 속성에 접근

# 인스턴스 공유 방지하려면, 인스턴스 속성으로 만들 것.
class Person:
    ''' person class.'''
    __bag = 'none' #비공개 클래스 속성

    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

    def greeting(self):
        ''' greeting method.'''
        print('hello!')

james = Person()
james.put_bag("book")

maria = Person()
maria.put_bag("pen")

print(james.bag)
print(maria.bag)

print(Person.__doc__) # person 클래스의 독스트링
print(Person.greeting.__doc__) #greeting method의 독스트링


