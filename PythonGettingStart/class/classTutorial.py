class Person:
    def greeting(self):
        print('hello.')

james = Person()

print(james)
james.greeting()

# 빈 클래스
class Emplt:
    pass


# 메서드 안에서 메서드 호출
class Person:
    def greeting(self):
        print('hello.')

    def hello(self):
        self.greeting() #self.메서드명()

james = Person()
james.hello()


# 특정 클래스의 인스턴스인지 확인  isinstance(인스턴스, 클래스)
print(isinstance(james, Person))

