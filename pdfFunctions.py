def createPdfID(pdfNamesList):
    pdfToID = {}
    idToPdf = {}
    i = 0
    for pdfName in pdfNamesList:
        pdfToID[i] = pdfName
        idToPdf[pdfName] = i
        i += 1
    return pdfToID, idToPdf

def getPdfFromID(id, idToPdf):
    return idToPdf[id]


def getIDFromPdf(pdf, pdfToID):
    return pdfToID[pdf]


#Counts words in a text 
def countWordsInText(text):
    words = text.split() 
    return len(words)

#recieves an array with all the texts and returns a list of id for each 
def createIdList(texts): 
    documentIdList = [] 
    i = 0 
    for text in texts: 
        documentIdList.append(i) 
        i+= 1 
    return documentIdList 


'''
pdfList = ['apple','app','ape','banana','bat','ball','cat','car','dog']

idToPdf, pdfToID = createPdfID(pdfList)
print(getPdfFromID(5,idToPdf))
print(getIDFromPdf('banana',pdfToID))
'''

#Falta agregar longitud del PDF para calcular porcentaje 
