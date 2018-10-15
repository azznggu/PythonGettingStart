# list control

# append - 리스트에 요소 추가
a = [10, 20]
a.append(30)
print(a)

#append(list)
a.append([40,50])
print(a)

#extend - 다른 리스트 연결
a.extend([60,70])
print(a)

#insert - 특정 위치에 값 추가
a.insert(0, 1)
print(a)
a.insert(7, 80)
print(a)

#remove - 특정 값 제거
a.remove(20)
a.remove([40,50])
print(a)

#pop - 맨마지막 값 삭제 후 삭제값 반환
print(a.pop())

#index - 특정 값의 인덱스 반환
print(a.index(30))

#count - 특정 값 개수 반환
print(a.count(60))

#reverse
a.reverse()
print(a)

#sort
a.sort()
print(a)

#clear - 모든 리스트 삭제
a.clear()
print(a)

#인덱스 활용하여 리스트 요소 조작
a = [1,2,3]
a[len(a):] = [10]
print(a)

#del - 특정 인덱스 값 삭제

del a[0]
print(a)