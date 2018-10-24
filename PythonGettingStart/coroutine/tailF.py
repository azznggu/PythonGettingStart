import time

# tail -f 흉내낸 generator
def follow(file):
    file.seek(0, 2) # 포지션을 파일 맨 끝으로 이동
    while(True):
        line = file.readline()
        if not line :
            time.sleep(0.1)
            continue
        yield line  #line 있으면 yield로 상위 블록으로 넘겨줌


logfile = open('test.txt', 'r')
for line in follow(logfile):
    print(line, end=' ')
