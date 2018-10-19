# method overriding - parent 메소드보다 child 메소드를 우선하다. parent의 동일 메소드를 무시하다.(확장)
# 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용

class Person:
    def greeting(self):
        print('hello')

class Student(Person):
    def greeting(self):
        super(Student,self).greeting() #parent로부터 필요한 or 중복될 수 있는 기능 사용
        print('''I'm student''')


james = Student()
james.greeting()

