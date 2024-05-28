import vectorizeWordDiego as vwd
import trie as t
import load
import cleanText
import search
import pdfFunctions

path = '/Users/diegoforni/Documents/ProjectoFinalAlgo2/pdfs'

pdfNames = load.namesPDFs(path)

texts = load.convertPDFs(pdfNames, path)

texts1 = texts



def closestWords(matrix, words):
    closest = []
    for word in words:
        closest.append(word)
        closeWords = vwd.getClosestWords(matrix,word)
        for closeWord in closeWords:
            closest.append(closeWord)
        
    return closest

'''
def rankDocuments(trie,words,cantTextos):
    documents = {}
    for i in range(cantTextos):
        documents[i] = 0
    dictWords = t.searchTrieDict(trie,words)
    for word in dictWords:
        if dictWords[word] is not None:
            for doc in dictWords[word]:
                documents[doc] += 1
    return documents
'''


texts = vwd.splitTexts(texts)
for text in range(len(texts)):
    texts[text] = cleanText.cleanText(texts[text])
matrix = vwd.fillMatrix(texts)
        





strInput = "gatos"
strInput = cleanText.cleanText(strInput)

arrayInput = []

for word in strInput:
    if vwd.existInMatrix(matrix, word):
        arrayInput.append(word)
        
#print(arrayInput)

#words = closestWords(matrix,arrayInput)

#print("words: ",words)

words = cleanText.cleanText("gatos")

documentsId = [0,1,2]
pdfToId, idToPdf = pdfFunctions.createPdfID(pdfNames)

texts1[0] = "rosario es una ciudad de argentina, comen gatos"
texts1[1] = "el poker es un juego de cartas muy popular"
texts1[2] = "las mascotas mas comunes son perros y gatos"

T = t.Trie()
array1 = cleanText.cleanText(texts1[0]) 
t.insertMainTrie(T,array1,0)

array2 = texts1[1]
array1 = cleanText.cleanText(texts1[1]) 

t.insertMainTrie(T,array2,1)

array3 = texts1[2]
array1 = cleanText.cleanText(texts1[2]) 

t.insertMainTrie(T,array3,2)
t.printTrie(T.root,0)


print(search.rankDocuments(words,T,3,documentsId,texts1,pdfToId))

#palabras = cleanText.cleanText("manos cartas valor")
#print(t.searchTrieDict(T,palabras))

#print(rankDocuments(T,words,4))



