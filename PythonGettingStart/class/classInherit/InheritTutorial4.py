# 다중 상속

class Person:
    def greeting(self):
        print('hello.')

class University:
    def manage_credit(self):
        print('credit managing.')

class Undergraduate(Person, University):  # inherits 2 parent class
    def study(self):
        print('studying.')

james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()



class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
 
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')
 
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
 
class D(B, C):
    pass
x = D()
x.greeting()    # 안녕하세요. B입니다.
#기반 클래스 A가 있고, B, C가 A를 상속받습니다. 다시 D가 B, C를 상속

'''
많은 프로그래밍 언어들이 다이아몬드 상속에 대한 해결책을 제시하고 있는데 
파이썬에서는 메서드 탐색 순서(Method Resolution Order, MRO)를 따릅니다.
메서드 mro를 사용해보면 메서드 탐색 순서가 나옵니다(클래스.__mro__ 형식도 같은 내용)
파이썬은 다중 상속을 한다면 class D(B, C):의 클래스 목록 중 왼쪽에서 오른쪽 순서로 메서드를 찾습니다. 
그러므로 같은 메서드가 있다면 B가 우선합니다. 
만약 상속 관계가 복잡하게 얽혀 있다면 MRO를 살펴보는 것이 편리합니다.
'''
print(D.mro())

#object 클래스 -> 모든 클래스의 base
print(int.mro())

#모든 클래스는 object 클래스를 상속받으므로 기본적으로 object를 생략
class x:
    pass

class x(object):
    pass