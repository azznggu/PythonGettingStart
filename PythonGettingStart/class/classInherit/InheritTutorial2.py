#기반 클래스의 속성 사용

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'

class Student(Person):
    def __init__(self):
        print('Student__init__')
        self.school = 'school'

james = Student()

print(james.school)
#print(james.hello)  # ->  AttributeError("'Student' object has no attribute 'hello'",)

#base 클래스의 속성 hello가 init으로부터 설정되지 않았기때문에 attributeError발생.
#child 클래스가 init호출 안 할 경우에는 base 클래스의 init이 호출되므로 문제 없음.

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'

class Student(Person):
    def __init__(self):
        print('Student__init__')
        #super().__init__()  # super()로 base클래스의 init을 호출.
        super(Student, self).__init__()  #super()보다 명시적으로 호출하는 경우.
        self.school = 'school'

james = Student()

print(james.school)
print(james.hello)