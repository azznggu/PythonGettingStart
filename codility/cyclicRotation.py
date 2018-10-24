
def cyclicRotate(A, K):
    if K == 0:
        return A
    resultList = []
    for i in range(len(A)):
        resultList.append(A[i-1])
    K -= 1
    return cyclicRotate(resultList, K)
        





A = [1, 2, 3]
print('target list: ', A)
K = int(input('Enter rotation count: '))
result = cyclicRotate(A, K)
print(result)