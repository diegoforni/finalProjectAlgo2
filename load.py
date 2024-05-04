from trie import * 
from pdfFunctions import *
import pickle
import os    

from cleanText import cleanText

#Acá va la función que recibe una lista de pdf para insertar en el Trie 

#recibo una lista de pdfs y los inserto en el trie
def namesPDFs():
    listNamesPDFs = []
    listNamesPDFs = os.listdir("C:\\Users\\Facultad Juli\\Documents\\GitHub\\finalProjectAlgo2\\pdfs")
    return listNamesPDFs

#"C:\\Users\\Facultad Juli\\Documents\\GitHub\\finalProjectAlgo2\\pdfs\\" + listPDFs[0]
def convertPDFs(listPDFs):
    listTexts = []
    for i in range(len(listPDFs)):
        print("aca entra")
        text = ''
        with open("C:\\Users\\Facultad Juli\\Documents\\GitHub\\finalProjectAlgo2\\pdfs\\" + listPDFs[i], 'rb') as file:
            # Lee el contenido del archivo PDF como una cadena binaria
            pdf_content = file.read()
            try:
                # Intenta decodificar el contenido del PDF como UTF-8
                text = pdf_content.decode('utf-8')
            except UnicodeDecodeError:
                # Si no se puede decodificar como UTF-8, intenta Latin-1
                try:
                    text = pdf_content.decode('latin-1')
                except UnicodeDecodeError:
                    # Si aún hay un error, simplemente regresa el texto vacío
                    pass
        listTexts.append(text)
    return listTexts

def loadInTrie():
    
    listPDFs = namesPDFs()  #lista de nombres de los pdfs
    listTexts = convertPDFs(listPDFs) #lista de textos de los pdfs como strings
    #limpio todos los textos
    for i in range(len(listPDFs)):
        listTexts[i] = cleanText(listTexts[i])
    #return listTexts 
    #creo una lista con los IDs de los pdfs
    idToPdf, pdfToID = createPdfID(listPDFs)
    ids = []
    for i in range(len(listPDFs)):
        ids.append(getIDFromPdf(listPDFs[i],pdfToID))
        
    #inserto en el trie
    trie = Trie()
    for i in range(len(listTexts)): 
        insertMainTrie(trie,listTexts[i],ids[i])
    
    return trie
         
print(loadInTrie()[0])
#loadInTrie()
#print(T.root.children[0].children[0].children[0].children[0].children[0].appearances)