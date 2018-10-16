# dictionary expression
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)


# key<->value change
t = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = {value: key for key, value in t.items()}
print(y)


# 특정 값이 있는 키:값 삭제
t = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

#error case
#RuntimeError('dictionary changed size during iteration',)
#for key, value in t.items():
#    if value == 20:
#        del t[key]

#삭제 대신 해당 제외한 새로운 dictionary 생성
new = {key: value for key, value in t.items() if value !=20}
print(new)



# dictionary in dictionary -> [key][key] -> 계층형 데이터 구조에 사용
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

mars_mean_radius = terrestrial_planet['Mars']['mean_radius']
print(mars_mean_radius)