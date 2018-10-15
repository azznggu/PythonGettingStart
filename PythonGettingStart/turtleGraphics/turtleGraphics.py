import turtle as t

def drawPolygon():
    t.shape('turtle')
    t.color('red')
    angle = int(input("which one to draw? :"))
    t.begin_fill()
    for i in range(angle):
        t.forward(100)
        t.right(360/angle)
    t.end_fill()


def drawCircle1():
    t.shape('triangle')
    for i in range(100):
        t.circle(0+i)

def drawCircle2():
    n = 60
    t.shape('circle')
    t.speed('fastest')
    for i in range(n):
        t.circle(100)
        t.left(360/n)

'''
5각형을 그릴 때는 72도(360 / 5)를 회전합니다. 
이때 별 꼭지점은 72도를 한 번 더 회전해서 144도입니다. 
따라서 t.forward(100)으로 선을 한 번 그리고 
t.right((360 / n) * 2)으로 오른쪽으로 144도 회전한 뒤 t.forward(100)으로 선을 그립니다. 
그리고 별 꼭지점을 그린 뒤 다음 꼭지점을 그릴 때는 t.left(360 / n)으로 왼쪽으로 72도 회전합니다. 
이렇게 5번 반복하면 오각별을 그릴 수 있습니다.
'''
def drawStar():
    n=5
    for i in range(5):
        t.shape('turtle')
        t.forward(100)
        t.right(360/n*2)
        t.forward(100)
        t.left(360/n)


#drawPolygon()
#drawCircle1()
#drawCircle2()
drawStar()