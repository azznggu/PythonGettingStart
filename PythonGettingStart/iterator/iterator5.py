# 특정수의 배수를 만드는 iterator (배수는 0부터 지정된 숫자보다 작을때까지)
class MultipleIterator:
    def __init__(self, stop, multiple):
        self.current = 0
        self.stop = stop
        self.multiple = multiple

    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 1
        if self.current * self.multiple < self.stop:
            return self.current * self.multiple
        else:
            raise StopIteration 

for i in MultipleIterator(20, 3):
    print(i, end=' ')

print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')