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


'''
pdfList = ['apple','app','ape','banana','bat','ball','cat','car','dog']

idToPdf, pdfToID = createPdfID(pdfList)
print(getPdfFromID(5,idToPdf))
print(getIDFromPdf('banana',pdfToID))
'''

#Falta agregar longitud del PDF para calcular porcentaje 
