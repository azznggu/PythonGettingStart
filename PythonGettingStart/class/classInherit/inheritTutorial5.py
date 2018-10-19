'''
추상 클래스 - 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용
              인스턴스를 만들 때는 사용하지 않으며 오로지 상속에만 사용
              그리고 파생 클래스에서 반드시 구현해야 할 메서드를 정해 줄 때 사용
              추상 클래스는 인스턴스화 불가.(에러 - TypeError: Can't instantiate abstract class)
from abc import *   #abstract base class 모듈로부터 모든 클래스, 메서드 import

class 추상클래스이름(metaclass=ABCMeta):

    @abstractmethod
    def 메서드이름(self):
        코드
'''
from abc import *
class StudentBase(metaclass = ABCMeta):

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print("studying")

    #def go_to_school(self):
    #    print("going to school")
    # 추상클래스를 상속받는 파생 클래스의 인스턴스를 만들 때 확인.
    # @abstractmethod가 붙은 추상 메서드 미작성시 에러 발생.
    # -> TypeError("Can't instantiate abstract class Student with abstract methods go_to_school",)

student = Student()
student.study()

