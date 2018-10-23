# 문자열 검색 코루틴
def find(word):
    result = False
    while True:
       input = (yield result)
       result = word in input

f = find('Python')
next(f)
 
print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python Script'))
 
f.close()
