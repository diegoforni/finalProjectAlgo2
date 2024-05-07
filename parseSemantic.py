wordEndings = {
    "ción": len("ción"),
    "dor": len("dor"),
    "dora": len("dora"),
    "doras": len("doras"),
    "ría": len("ría"),
    "adada": len("adada"),
    "ado": len("ado"),
    "adaje": len("adaje"),
    "ación": len("ación"),
    "adición": len("adición"),
    "aducción": len("aducción"),
    "adura": len("adura"),
    "aección": len("aección"),
    "aepción": len("aepción"),
    "aido": len("aido"),
    "aión": len("aión"),
    "amiento": len("amiento"),
    "ancia": len("ancia"),
    "anión": len("anión"),
    "ascripción": len("ascripción"),
    "asición": len("asición"),
    "asión": len("asión"),
    "dad": len("dad"),
    "tad": len("tad"),
    "bilidad": len("bilidad"),
    "edad": len("edad"),
    "era": len("era"),
    "ería": len("ería"),
    "ez": len("ez"),
    "eza": len("eza"),
    "ía": len("ía"),
    "idad": len("idad"),
    "ancia": len("ancia"),
    "ura": len("ura"),
    "dor": len("dor"),
    "dero": len("dero"),
    "ero": len("ero"),
    "ista": len("ista"),
    "ado": len("ado"),
    "ario": len("ario"),
    "ía": len("ía"),
    "ero": len("ero"),
    "ería": len("ería"),
    "able": len("able"),
    "ar": len("ar"),
    "áceo": len("áceo"),
    "aco": len("aco"),
    "al": len("al"),
    "áneo": len("áneo"),
    "ante": len("ante"),
    "ario": len("ario"),
    "ente": len("ente"),
    "iente": len("iente"),
    "ento": len("ento"),
    "érrimo": len("érrimo"),
    "ible": len("ible"),
    "ico": len("ico"),
    "ífico": len("ífico"),
    "il": len("il"),
    "ino": len("ino"),
    "ísimo": len("ísimo"),
    "ear": len("ear"),
}

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
