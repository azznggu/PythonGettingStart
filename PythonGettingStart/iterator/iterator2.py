'''
iterator 만들기

class 이터레이터이름:
    def __iter__(self):
        코드
 
    def __next__(self):
        코드
'''

#range 처럼 동작하는 iterator 작성
class Counter:
    def __init__(self, stop):
        self.current = 0  # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop  # 반복을 끝낼 숫자
    
    def __iter__(self):
        return self       # 현재 인스턴스를 반환

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else : 
            raise StopIteration

#for i in Counter(3):
#    print(i)


# iterator unpacking
# Counter()의 결과를 변수 여러 개에 할당
a, b, c = Counter(3)
print(a,b,c)


# map도 iterator-> 변수 여러개에 값 할당 가능. 
a, b, c = map(int, input().split())