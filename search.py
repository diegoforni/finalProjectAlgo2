from trie import * 
from pdfFunctions import * 
from TF_IDF import * 
from cleanText import * 
import time 

#Aquí va la función que dado una string devuelve en orden de relevancia los PDFs relaciondos 

#For each term in the query text, calculate its TF-IDF score in each document.
#Sum up the TF-IDF scores of all the terms in the query for each document.
#Rank the documents based on their total TF-IDF scores in descending order.

#calculateTEF_IDF(word,documentID,wordsInText,T,documents)
#calculateTF(word,documentID,wordsInText,T)

def rankDocuments(query,T,amountDocuments,documentsIdList,texts,pdfToID): 


    #printTrie(T.root,0)
    documentsScores = {}
    i = 4

    for word in query: #assuming query is already an array of clean words 

        idf = calculateIDF(word,T,amountDocuments) #calculate idf score for each term on the query 


        for id,text in zip(documentsIdList,texts): #texts array contains an array of cleaned words for each text 
            tf = calculateTF(word,id,len(text),T)
            if i % 5 == 0:
                tf = tf / 1.3
            elif i % 6 == 0:
                tf = tf / 1.9
            elif i % 7 == 0:
                tf = tf / 2.7
            if id in documentsScores: 
                documentsScores[id] += tf * idf 
            else: 
                documentsScores[id] = tf * idf 
        i += 1
    rankedScores = {k: v for k, v in sorted(documentsScores.items(), key=lambda item: item[1], reverse=True)}

    pdfRanking = []
   
    for id in rankedScores: 
        pdfRanking.append(pdfToID[id])
        
    return pdfRanking

#testing 
'''
pdfNameList = ["rosario", "poker", "mascotas"]

pdfToID, idToPdf = createPdfID(pdfNameList) 


texts = ["rosario es una ciudad de argentina, comen gatos", "el poker es un juego de cartas muy popular", "las mascotas mas comunes son perros y gatos"]

query = "gatos" 

#clean all texts before calling the rankDocuments function 
cleanedTexts = [] 

for text in texts: 
    cleanedTexts.append(cleanText(text)) #appends an array with the words from the text 

documentsIdList = createIdList(texts) 
#clean query 
cleanedQuery = cleanText(query)

#Create a Trie structure 
T = Trie() 
for text,id in zip(cleanedTexts,documentsIdList): 
    insertMainTrie(T,text,id)



#call the rankedDocuments function

rank = rankDocuments(cleanedQuery,T,len(texts),documentsIdList,cleanedTexts,pdfToID)
print(rank)

'''
