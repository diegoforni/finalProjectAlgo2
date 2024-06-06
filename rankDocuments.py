import vectorizeWordDiego as vwd
import trie as t
import load
import cleanText
import searchRank
import pdfFunctions
import pickle

def closestWords(matrix, words):
    closest = []
    for word in words:
        closest.append(word)
        closeWords = vwd.getClosestWords(matrix,word)
        for closeWord in closeWords:
            closest.append(closeWord)
        
    return closest


        

def checkWordInMatrix(matrix,strInput):
    arrayInput = []
    for word in strInput:
        if vwd.existInMatrix(matrix, word):
            arrayInput.append(word)
    return arrayInput


def rankDocuments(consulta, texts,T,amountDocuments, pdfNames,lengthTexts):

    with open("matrix", "rb") as f:
        matrix = pickle.load(f)    
    
    arrayInput = checkWordInMatrix(matrix,consulta)
    if len(arrayInput) == 0:
        return "Document not found"
    else:
        closest = closestWords(matrix,arrayInput)
        print(closest)
        documentsIdList = list(range(amountDocuments))
        pdfToId, idToPdf = pdfFunctions.createPdfID(pdfNames)
        return searchRank.rankDocuments(closest,T,amountDocuments,documentsIdList,lengthTexts,pdfToId)
    
    