#mine
#class AdvancedList(list):
#    def replace(self, a, b):
#        for i in range(len(self)):
#            if self[i] == a:
#                self[i] = b

#solution
'''
특정 값을 찾을 때는 리스트의 index 메서드를 사용하고, 
index로 찾은 인덱스를 self에 지정해준 뒤 새 값을 할당하면 값을 바꿀 수 있습니다. 
이때 리스트에서 같은 값이 여러 개 들어있을 수도 있으므로 모든 값을 바꿔주어야 합니다. 
따라서 while로 self에 특정 요소가 있을 때 계속 반복하도록 만든 뒤 요소를 바꿔주면 됩니다. 
특정 요소가 있는지 확인할 때는 in 연산자를 사용하거나 
self.count(찾을값)처럼 count 메서드를 사용해도 됩니다
'''

class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new

x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)



