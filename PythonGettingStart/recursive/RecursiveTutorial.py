#
def test() :
    print("hi!")
    test()

#test() -> 실행시 RecursionError: maximum recursion depth exceeded while pickling an object
#           스택 메모리 사용 초과(stack overflow)
#-> 재귀함수 사용 시 종료 조건 작성 필요.

def hello(count):
    if count == 0:
        return
    print("hello!")
    count -=1
    hello(count)

#hello(5)


#팩토리얼
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

#print(factorial(5))


#재귀호출 이용한 회문 판별
def is_palindrome(word):
    if len(word) < 2:
        return  True
    if word[0] != word[-1]:
        return False

    return is_palindrome(word[1:-1])

print(is_palindrome('level'))



