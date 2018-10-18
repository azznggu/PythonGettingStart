#공개속성(public)과 비공개속성(private)


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet #__ -> 비공개 속성 : 비공개 속성은 클래스 바깥에 드러내고 싶지 않은 값에 사용
    
    def pay(self, amount):
        self.__wallet -= amount
        print('잔액 {0}'.format(self.__wallet))

    def __greeting(self):
        print('hello {0}'.format(self.name))
              


park = Person('park',29,'miyazakidai', 1000)
print(park.name)
#print(park.__wallet) # 비공개 속성(private)은 접근 불가. AttributeError("'Person' object has no attribute '__wallet'",)

park.pay(300)


#비공개 메서드
#park.__greeting() # 비공개 메서드(private) 접근 불가. AttributeError





class knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    
    def slash(self):
        print('베기')

x = knight(health='500', mana='300', armor='50')
print(x.health, x.mana, x.armor)
x.slash()
