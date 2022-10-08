"""
Wordle Solver
"""
def validate(word, placedLetters, unplacedLetters, invalidLetters) :
    for i in unplacedLetters :
        if word.find(i) == -1 :
            return False
    for i in range(5) :
        if placedLetters[i] == '_' :
            continue
        if placedLetters[i] != word[i] :
            return False
    for i in invalidLetters :
        if word.find(i) != -1 :
            return False
    return True

f = open("Words.txt", 'r')
words = f.readlines()
#print(words)
placedLetters = input("Placed letters : ")
unplacedLetters = input("Unplaced letters : ")
invalidLetters = input("Invalid letters : ")
for i in range(len(words)) :
    b = False
    if validate(words[i], placedLetters, unplacedLetters, invalidLetters) :
        print(words[i], end = '')
