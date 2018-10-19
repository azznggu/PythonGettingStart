class Person:
    def greeting(self):
        print("hello")

class Student(Person):
    def study(self):
        print("studying")

#Student is a Person (is-a 관계-> 상속)
park = Student()
park.greeting()
park.study()

class PersonList():
    def __init__(self):
        self.person_list = []

    def append_person(self, person):
        self.person_list.append(person)

#PersonList has a Person (has-a 관계->인스턴스 넣는 포함 방식)       
james = Person()
personlist = PersonList()
personlist.append_person(james)
personlist.person_list[0].greeting()


#파생클래스인지 확인
print(issubclass(Student,Person))



