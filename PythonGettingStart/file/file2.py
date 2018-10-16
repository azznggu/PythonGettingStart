
#python 객체 write, read 모듈

import pickle

name = 'park'
age = 29
address = 'kawasaki-shi, miyamae-ku'
score = {'korean' : 90, 'math' : 33, 'history' : 88}

def save():
    with open('park.p', 'wb') as file:
        pickle.dump(name, file)
        pickle.dump(age, file)
        pickle.dump(address, file)
        pickle.dump(score, file)

def read():
    with open('park.p', 'rb') as file:
        name = pickle.load(file)
        age = pickle.load(file)
        address = pickle.load(file)
        score = pickle.load(file)

        print(name)
        print(age)
        print(address)
        print(score)

read()



'''
file mode type
 r
 w
 a
 rb
 wb

'''
