def solution(A):
    print('ing.')
    for i in range(len(A)):
        if not i+1 in A:
            return i+1
        else:
            continue

# solution 100%
def solution2(A):
    return sum(range(len(A)+2))-sum(A) # range시 0까지포함되므로 다음수까지 더하려면 +2
# ex)
#   A = [2, 3, 1, 5]                                sum(A)       =     2 + 3 + 1 + 5 
#   range(len(A)+2)  range(6) -> 0, 1, 2, 3, 4, 5   sum(range(6) = 0 + 1 + 2 + 3 + 4 + 5
#   sum(range(6))-sum(A) = 4 , 없는 수만 return됨 



A = [2,3,1,5]
test = solution2(A)
print(test)
#list = list(range(6))
#print(list)

