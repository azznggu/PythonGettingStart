def palindromeCheck() :
    word = input('Enter word to check: ')
    flag = True

    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            flag = False
            break
    return flag

def TwoGramCheck() :
    word = input('Enter word to check: ')
    count = 0
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            print(word[i])
            count += 1
    return count

def TwoGramWordCheck() :
    words = input('Enter sentence to check:').split(' ')
    count = 0
    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            print(words[i])
            count += 1
    return count

def NGramWordChecker():
    n = int(input('Enter number: '))
    text = input('Enter text: ')
    words = text.split(' ')

    if(n > len(words)):
        print('wrong')
    else:
        for i in range(len(words)-(n-1)):
            for j in range(n):
                print(words[i+j], end = ' ')
            print()
       

#print(palindromeCheck())
#print('string count: '+str(TwoGramCheck()))
#print('word count: '+str(TwoGramWordCheck()))
NGramWordChecker()