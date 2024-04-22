wordEndings = {
    "ción" : 4,
    "dor": 3,
    "dora": 4,
    "doras": 5,
    "ría": 3,
}
maxLen = 0

for key in wordEndings:
    if len(key) > maxLen:
        maxLen = len(key)

def parseSemantic(word):
    length = len(word) #O(1)
    endOfWord = ''
    if length < maxLen:
        return word
    for i in range(maxLen): 
        endOfWord = word[length-i-1] + endOfWord
        # buscar en diccionario
        if endOfWord in wordEndings: #O(1)
            # cortar la palabra
            word = word[:length - wordEndings[endOfWord]]
            newLength = len(word)
            if word[newLength-1] == 'a' or word[newLength-1] == 'o':
                word = word[:newLength-1] + '@'
            return word
    return word
 

print(parseSemantic('fumador'))
print(parseSemantic('fumadores'))
print(parseSemantic('fumador'))

