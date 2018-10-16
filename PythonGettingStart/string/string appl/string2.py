## access by index
#hello = "hello!"
#print(hello[0])
#print(hello[-1])
#print(hello[len(hello)-1])

#print(hello[0:5])
#print(hello[3:])
#print(hello[3:-1])
#print(hello[:])

#for i in hello:
#    print(i, end='.')


 
# string control

s = 'sample text to test.'

#1.replace
replaced = s.replace('sample', 'string')
print('orign: '+s)
print('replaced: '+replaced)

#2.split
s = 'apple,pear,grape,pineapple'
splitted = s.split(',')
print('orign: '+s)
print(splitted)

#3.join -> 구분자문자.join(리스트or튜플)
a = '-'
joined = a.join(splitted)
print(joined)

#4.upper lower
print(joined.upper())
print(joined.lower())

#5.lstrip rstrip strip -> 공백 제거
s = '    python    '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

# 특정 문자 제거
s = 'aaPYTHONbb'
print(s.lstrip('a'))
print(s.rstrip('b'))
print(s.strip('ab'))

#6.zfill - 지정길이에 맞춰 문자열 왼쪽에 0 채우기
print('35'.zfill(2))
print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(6))

#7.find rfind -특정 문자 검색, 있으면 인덱스 반환. 없으면 -1 반환. rfind는 오른쪽부터 검색
s = 'apple pineapple'
print(s.find('ple'))
print(s.rfind('ple'))
print(s.find('nope'))

#8.index rindex - 특정 문자 검색 후 있으면 인덱스 반환, 없으면 에러 발생.
print(s.index('ple'))
print(s.rindex('ple'))
#print(s.index('nope')) -> 에러 발생.

#9.count -> 특정 문자 몇번 나오는지
print(s.count('ple'))



