# 정규표현식

import re

# match 함수 (정규표현식 패턴, 판단할 문자열) -> 문자열 처음부터 매칭확인. 문자열 있으면 match(SRE_match)객체 반환.
result = re.match('hi','hi python.')
print(result)

# 문자열 함수 find 로도 가능하지만(ex) 'Hello, world!'.find('Hello')), 
# 문자열 함수에서 할 수 없는 경우 정규표현식 활용.


#search 함수 -> 문자열 일부분이 매칭되는지 판단
# ^문자열 : 문자열이 맨앞에 오는지 판단
# 문자열$ : 문자열이 맨뒤에 오는지 판단

string = "hello python! I'm Park."
head = re.search('^hello', string)
print(head)
tail = re.search('Park.$', string)
print(tail)

#여러 문자열(문자) 중 하나라도 포함되어 있는지 판단
#이때는 |를 사용하여 문자열을 나열. 기본 개념은 OR 연산자와 동일
hasAtleastOne = re.match('Park.', string)
print(hasAtleastOne)