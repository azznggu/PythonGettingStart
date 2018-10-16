print('%s'%'hello Python.')
print('hello %s'%'Python.')
print('%s %s'%('hello','python.'))
print('%d%f'%(100,3.5))


#format
print('hello, {} {} {}'.format('python', 'script', 3.6))
print('hello, {0} {1} {2}'.format('python', 'script', 3.6))
print('hello, {0} {2} {1}'.format('python', 'script', 3.6))
print('{0} {0} {2} {1}'.format('python', 'script', 3.6))

print('hello, {language} {version}'.format(language='python', version=3.6))


#f -> formmating
language = 'python'
version = 3.6
print(f'hello {language} {version}!')


print('{{{0}}}'.format('python'))


#
print('%03d'%1)
print('%03d'%55)
print('{0:03d}'.format(35))

print('%.3f'%2.3)
print('{0:.3f}'.format(2.3))


#파일 경로에서 파일명만 가져오기
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'

#way1 split후 리스트 마지막 인덱스 값 출력
list = path.split('\\')
print(list[-1])

#way1.1 split후 reverse-> 첫번째값 출력
list = path.split('\\')
list.reverse()
print(list[0])

#way2 find함수->슬라이싱으로 특정 부분만 출력
print(path[path.rfind('python.exe'):])




