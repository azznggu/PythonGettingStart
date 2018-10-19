from math import sqrt
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point2D(x=10, y=20)
p2 = Point2D(x=30, y=50)

print('p1: {} {}'.format(p1.x, p1.y))
print('p2: {} {}'.format(p2.x, p2.y))

a = abs(p1.x-p2.x) #내장함수 abs로 정수 절대값 반환. c.f) math.fabs -> 실수 절대값 반환.
b = abs(p1.y-p2.y)
c = sqrt(a**2 + b**2)
#c = sqrt(pow(a,2)+pow(b,2))
#c = sqrt(a*a + b*b)
#print('distance: {}'.format(c))

print('distance :  {}'.format(c))


#namedtuple
'''
파이썬에서는 각 요소에 이름을 지정해 줄 수 있는 namedtuple을 제공합니다(collections 모듈). 
namedtuple은 자료형 이름과 요소의 이름을 지정하면 클래스를 생성해줍니다. 
여기서 자료형 이름은 문자열, 요소의 이름은 문자열 리스트를 넣어줍니다.
클래스 = collections.namedtuple('자료형이름', ['요소이름1', '요소이름2'])
namedtuple로 생성한 클래스는 값을 넣어서 인스턴스를 만들 수 있으며 
인스턴스.요소이름 또는 인스턴스[인덱스] 형식으로 요소에 접근할 수 있습니다.

인스턴스 = 클래스(값1, 값2)
인스턴스 = 클래스(요소이름1=값1, 요소이름2=값2)
인스턴스.요소이름1
인스턴스[인덱스]
'''
import collections

Point2D = collections.namedtuple('Point2D', ['x','y'])
p1 = Point2D(x = 10 , y = 20)
p2 = Point2D(x = 30 , y = 40)
a = p1.x - p2.x
b = p1.y - p2.y
c = sqrt(a*a + b*b)
print(c)

