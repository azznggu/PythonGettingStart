class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __getitem__(self, index):
        #반복을 끝낼 조건을 만들어야 하는데 반복을 끝낼 초 self.stop만 판단하면 안 됩니다. 
        #이때는 시작하는 초와 반복을 끝낼 초 안에서만 인덱스로 접근할 수 있어야 하므로 
        #반복을 끝낼 초에서 시작하는 초를 빼야 합니다
        if index < self.stop - self.start:
            #반환할 시간값은 시작하는 초가 있으므로 self.start에 index를 더해서 만듭니다
            #self.start+index 는 초 값이므로 시, 분, 초에 따라 변환 필요.
            #시
            #self.start+index 는 초 값이므로 60으로 나누면(//) 분 단위. 여기서 다시 60으로 나누었을때(//) 시간 단위. 여기서 24로 나누었을떄의 나머지가
            #시간값 표시에 해당.
            #분
            #self.start+index 는 초 값이므로 60으로 나누면(//) 분 단위. 여기서 다시 60으로 나누었을때의 나머지(%)가 분값 표시에 해당.
            #초
            #self.start+index 는 초 값이므로 60으로 나누었을때의 나머지(%)가 초값 표시에 해당.
            return '{0:02d}:{1:02d}:{2:02d}'.format((self.start+index)//60//60%24, (self.start+index)//60%60, (self.start+index)%60)
        else:
            raise IndexError


start, stop, index = map(int, input().split(' '))
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')