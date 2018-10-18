# static method
'''
class 클래스이름:
    @staticmethod
    def 메서드(매개변수1, 매개변수2):
        코드
정적 메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없습니다. 
그래서 보통 정적 메서드는 메서드 안에서 인스턴스 속성, 인스턴스 메서드를 사용하지 않아도 될 때 또는, 
인스턴스 자체가 필요없을 때 사용합니다.
'''
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)


Calc.add(10,20)
Calc.mul(10,20)


#class method
'''
class 클래스이름:
    @classmethod
    def 메서드(cls, 매개변수1, 매개변수2):
        코드

정적 메서드와 비슷하지만 약간의 차이점이 있음
'''
class Person :
    count = 0 # 클래스 속성

    def __init__ (self):
        Person.count += 1 # 인스턴스 생성 시 마다 클래스속성 count 1증가

    @classmethod
    def print_count(cls):
        print('{0}개 생성.'.format(cls.count))

james = Person()
maria = Person()

Person.print_count()


'''
파이썬 자료형의 인스턴스 메서드와 정적(클래스) 메서드
 인스턴스의 내용을 변경해야 할 때는 update와 같이 인스턴스 메서드로 작성하면 되고,
 인스턴스 내용과는 상관없이 결과만 구하면 될 때는 set.union과 같이 정적(클래스) 메서드로 작성
'''
#ex)
#인스턴스 메서드 사용
a = {1,2,3,4}
a.update({5})
print(a)

#정적(클래스)메서드 사용
print(set.union({1,2,3,4},{5}))