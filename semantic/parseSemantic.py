wordEndings = {
    "ción" : 4,
    "dor": 3,
    "dora": 4,
    "doras": 5,
    "ría": 3,
}
'''
Lo que hice fue sacar la validacion de que la longitud sea mas larga que la terminación mas larga, asi
simplemente usando la longitud que tenga la palabra, busca la raiz de la palabra
'''

def parseSemantic(word):
    length = len(word) #O(1)
    endOfWord = ''
    for i in range(len(word)):
        endOfWord = word[length-i-1] + endOfWord
        # buscar en diccionario
        if endOfWord in wordEndings: #O(1)
            # cortar la palabra
            word = word[:length - wordEndings[endOfWord]]
            newLength = len(word)
            ## si la palabra es vacía retorna ''
            if newLength == 0:
                return word
            if word[newLength-1] == 'a' or word[newLength-1] == 'o':
                word = word[:newLength-1] + '@'
            return word
    return word

print(parseSemantic('adoras'))
print(parseSemantic('fumador'))
print(parseSemantic('fumaría'))
print(parseSemantic('fumar'))

