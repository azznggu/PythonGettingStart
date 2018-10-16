def readFile():
    # read
    #file = open('hello.txt','r')
    #s = file.read()
    #print(s)
    #file.close()
    
    # 파일 객체 close-> 귀찮 -> 자동으로 닫기
    with open('hello.txt','r') as file:
        s = file.read()
        print(s)

def readLinesFromFile():
    with open('hello.txt','r') as file:
        lines = file.readlines()
        print(lines)

def readLineFromFIle():
    with open('hello.txt','r') as file:
        line = file.readline()
        print(line.strip('\n'))
        while line !='':
            line = file.readline()
            print(line.strip('\n'))

def writeFile():
    with open('hello.txt','w') as file:
        for i in range(3):
            file.write('write {0}\n'.format(i))


def writeListToFIle(list):
    with open('hello.txt','w') as file:
        file.writelines(list)


#writeFile()
list = ['hello.\n','writeTest\n','in python\n']
writeListToFIle(list)
readFile()
readLinesFromFile()
readLineFromFIle()

#file객체 -> iterator.  for 루프 가능. 여러 변수에 저장가능(unpacking)
file = open('hello.txt','r')
for i in file :
    print(i.strip('\n'))

file = open('hello.txt','r')
a,b,c = file
print(a, b, c)
