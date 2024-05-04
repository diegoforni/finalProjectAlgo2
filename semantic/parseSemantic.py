wordEndings = {

}

def parseSemantic(word):
    length = len(word) #O(1)
    if length == 0:
        return ''
    if word[length-1] == 's':
        return parseSemantic(word[:length-1])
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
