'''
인덱스로 접근할 수 있는 이터레이터 만들기

class 이터레이터이름:
 def __getitem__(self, 인덱스):   -> 클래스에 __getitem__ 메서드 구현 시 인덱스로 접근가능한 이터레이터가 됨.
     코드
'''

class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):   # 인덱스를 받음
        if index < self.stop:       # 인덱스가 반복을 끝낼 숫자보다 작을 때
            return index            # 인덱스 반환
        else:                       # 인덱스가 반복을 끝낼 숫자보다 크거나 같을 때
            raise IndexError        # 예외 발생


print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end = ' ')