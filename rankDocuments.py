import vectorizeWordDiego as vwd
import trie as t
import load
import cleanText
import search
import pdfFunctions

path = 'C:\\Users\\juana\\OneDrive\\Documents\\GitHub\\ProjectFinalAlgo2\\pdfs'

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
        

strInput = "bacteria enfermedad contagio"
strInput = cleanText.cleanText(strInput)

arrayInput = []

for word in strInput:
    if vwd.existInMatrix(matrix, word):
        arrayInput.append(word)

#print(arrayInput)

words = closestWords(matrix,arrayInput)

#print("words: ",words)

#words = cleanText.cleanText("argentina rosario ciudad")

documentsId = [0,1,2,3,4,5]

pdfToId, idToPdf = pdfFunctions.createPdfID(pdfNames)

#print(matrix['enfermedad'])

T = t.Trie()
array1 = cleanText.cleanText(texts1[0]) 
#print(array1)
t.insertMainTrie(T,array1,0)


array2 = cleanText.cleanText(texts1[1]) 
#print(array2)
t.insertMainTrie(T,array2,1)


array3 = cleanText.cleanText(texts1[2]) 
#print(array3)
t.insertMainTrie(T,array3,2)

array4 = cleanText.cleanText(texts1[3]) 
#print(array3)
t.insertMainTrie(T,array4,3)

array5 = cleanText.cleanText(texts1[4]) 
#print(array3)
t.insertMainTrie(T,array5,4)

array6 = cleanText.cleanText(texts1[5]) 
#print(array3)
t.insertMainTrie(T,array6,5)

#t.printTrie(T.root,0)

print(search.rankDocuments(words,T,6,documentsId,texts1,pdfToId))

#palabras = cleanText.cleanText("manos cartas valor")
#print(t.searchTrieDict(T,palabras))

#print(rankDocuments(T,words,4))



