'''
모듈: 특정 기능을 .py 파일 단위로 작성한 것
패키지: 특정 기능과 관련된 여러 모듈을 묶은 것
        보통 인터넷에 있는 패키지를 설치해서 사용
라이브러리: 파이썬에 기본적으로 설치된 모듈과 내장 함수를 묶어서 
            파이썬 표준 라이브러리(Python Standard Library, PSL)
'''


#import module
import math
print("pi: " + str(math.pi))

print("sqrt: " + str(math.sqrt(4)))

#import package module
import urllib.request
response = urllib.request.urlopen('https://www.google.com').status
print("status: " + str(response))


# set module name as ''
import math as m
print(m.sqrt(4))

# set package module name as ''
import urllib.request as req
print(req.urlopen('https://www.google.com').status)


#import part of module
from math import pi
print(pi)

from math import pi, sqrt
from math import *

from urllib.request import urlopen, Request
req = Request('https://www.google.com')
response = urlopen(req)
print(response.status)

from urllib.request import Request as r, urlopen as u


# module 해제, 리로드
import array
del array

import importlib
import array
importlib.reload(array)