a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

r = set.union(a,b)  # a|b
print(r)

r = set.intersection(a,b) # a&b
print(r)

r = set.difference(a,b) # a-b
print(r)

r = set.symmetric_difference(a,b) # a^b
print(r)


a = {1, 2, 3, 4}
a.update({5,6}) # a|=b
print(a)

a.intersection_update({3,4,5,6}) # a&=b
print(a)

a.difference_update({3}) # a-=b
print(a)

a.symmetric_difference_update({0,1,2,3,4}) # a^=b
print(a)


#issubset 다른 set의 부분 집합인지 확인 a<=b
a ={1,2,3,4}
print(a.issubset({1,2,3,4,5}))

#issuperset 다른 set의 상위집합인지 확인 a>=b
print(a.issuperset({1,2,3}))

#isdisjoint 다른set와 겹치지않는지 확인
print(a.isdisjoint({5,6,7,8}))


#len
a ={1,2,3,4}
print(len(a))

#add
a.add(5)
print(a)

a ={1,2,3,4}
#remove - 세트에서 특정 요소(값)를 삭제하고 요소가 없으면 에러를 발생
a.remove(3)
print(a)

#discard - 트에서 특정 요소(값)를 삭제하고 요소가 없으면 그냥 넘어감
a.discard(3)
print(a)

#pop - 세트에서 임의의 요소(값)를 삭제하고 해당 요소를 반환
a.pop()
print(a)

#clear - 세트 모든 요소 삭제
a.clear()
print(a)
