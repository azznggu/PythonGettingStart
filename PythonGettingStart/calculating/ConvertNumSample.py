'''진수 표현
2진수: 숫자 앞에 0b를 붙이며 0과 1을 사용합니다.
8진수: 숫자 앞에 0o(숫자 0과 소문자 o)를 붙이며 0부터 7까지 사용합니다.
16진수: 숫자 앞에 0x 또는 0X를 붙이며 0부터 9, A부터 F까지 사용합니다(소문자 a부터 f도 가능).
'''

#binary
binary = 0b1011
b_to_i = int(binary)
print(b_to_i)
print(bin(b_to_i))

#octal
octal = 0o123
o_to_i = int(octal)
print(o_to_i)
print(oct(o_to_i))

#hexa
hexa = 0x18A
h_to_i = int(hexa)
print(h_to_i)
print(hex(h_to_i))



#complex number(복소수)변환
#허수부는 숫자 뒤에 j를 붙입니다(수학에서는 허수를 i로 표현하지만 공학에서는 j를 사용)
sum = 1.2+1.5j
print(sum)

complexed = complex(1.2,1.5)
print(complexed)




#튜플을 사용, 전역변수 업데이트
#함수 내에서 global로 전역변수 변경은 피하도록.

a=0
b=0
c=0

def update_global() :
    return(a+1, b+2, (c+1)*4)

print(a,b,c)
a,b,c = update_global()
print(a,b,c)


#multi assignment
a,b,c,d,e = 1,2,3,4,5
print(a,b,c,d,e)