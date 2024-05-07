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
    documentsScores = {}

    for word in query: #assuming query is already an array of clean words 

        idf = calculateIDF(word,T,amountDocuments) #calculate idf score for each term on the query 


        for id,text in zip(documentsIdList,texts): #texts array contains an array of cleaned words for each text 
            tf = calculateTF(word,id,len(text),T)
            if id in documentsScores: 
                documentsScores[id] += tf * idf 
            else: 
                documentsScores[id] = tf * idf 
 
    rankedScores = {k: v for k, v in sorted(documentsScores.items(), key=lambda item: item[1])}
    pdfRanking = []
   
    for id in rankedScores: 
        pdfRanking.append(pdfToID[id])
    return pdfRanking


#testing 
startTime = time.time()
pdfNameList = ["doc0", "doc1", "doc2","doc3", "doc4"]

pdfToID, idToPdf = createPdfID(pdfNameList) 


texts = ["El arte de la pintura ha sido una expresión humana desde tiempos antiguos. Desde las pinturas rupestres hasta las obras maestras renacentistas, el arte ha sido una forma de comunicar emociones y contar historias.", "La revolución industrial marcó un cambio fundamental en la sociedad y la economía. La introducción de la maquinaria y la producción en masa transformó las formas de trabajo y la vida de las personas.",
    "La poesía es un género literario que utiliza un lenguaje especial y la métrica para expresar sentimientos y emociones. Desde los sonetos de Shakespeare hasta las odas de Neruda, la poesía ha inspirado y conmovido a las personas a lo largo de la historia.","La exploración espacial ha sido un hito importante en la historia de la humanidad. Desde el lanzamiento del Sputnik hasta la llegada del hombre a la Luna, la exploración del espacio ha desafiado los límites de la ciencia y la tecnología.",
    "La gastronomía es una parte integral de la cultura de un país. Los platos tradicionales y las recetas transmitidas de generación en generación reflejan la historia y las influencias de una región.",
]

query = "Recetas de cocina saludable" 

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
endTime = time.time()

#print("excuted in: ", endTime-startTime, "seconds")




