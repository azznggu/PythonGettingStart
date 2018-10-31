def solutionMine(X, Y, D):
    count = 0
    while True:
        X += D
        count += 1
        if X < Y:
            continue
        else:
            break
    return count
    

def solution(X, Y, D):
    count = (Y - X) // D
    if (Y - X) % D > 0:
        return count + 1
    return count


x = 10
y = 70
d = 30

count = solution(x, y, d)
print(count)