print(10 == 10)
print(10 != 10)

a = 10
b = 10.0

print(a == b)
print(a is b)
print(a is not b)


print(id(a))
print(id(b))

result = bool(a is b)
print(result)