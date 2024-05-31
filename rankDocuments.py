import vectorizeWordDiego as vwd
import trie as t
import cleanText

def closestWords(matrix, words):
    closest = []
    for word in words:
        closest.append(word)
        closeWords = vwd.getClosestWords(matrix,word)
        for closeWord in closeWords:
            closest.append(closeWord)
        
    return closest


def splitTextsParagraphs(texts):
    texts = vwd.splitTexts(texts)
    for text in range(len(texts)):
        texts[text] = cleanText.cleanText(texts[text])
    return texts
        

def checkWordInMatrix(matrix,strInput):
    arrayInput = []
    for word in strInput:
        if vwd.existInMatrix(matrix, word):
            arrayInput.append(word)
    return arrayInput


def rankDocumentsTest(trie,words,cantTextos,pdfNames):
    documents = {pdfNames[i]: 0 for i in range(cantTextos)}
    for i in range(cantTextos):
        documents[i] = 0
    dictWords = t.searchTrieDict(trie,words)
    for word in dictWords:
        if dictWords[word] is not None:
            for doc in dictWords[word]:
                documents[pdfNames[doc]] += 1    
    
    documents = {k: v for k, v in documents.items() if v != 0}
                
    documents = sorted(documents.items(), key=lambda x: x[1], reverse=True)
    documents = [x[0] for x in documents]
    return documents


def getClosest(consulta,T,amountDocuments, pdfNames,matrix):
    arrayInput = checkWordInMatrix(matrix,consulta)
    if len(arrayInput) == 0:
        return "Document not found"
    else:
        closest = closestWords(matrix,arrayInput)
        print(closest)
        return rankDocumentsTest(T,closest,amountDocuments,pdfNames)
    
    