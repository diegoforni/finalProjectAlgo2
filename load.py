import trie
import pdfFunctions
import pickle
import os    
import cleanText

#crea una lista con los nombres de los pdfs, cada uno le va a tener que cambiar el path
def namesPDFs():
    listNamesPDFs = []
    listNamesPDFs = os.listdir("C:\\Users\\pc\\Documents\\GitHub\\ProjectFinalAlgo2\\pdfs")
    return listNamesPDFs

#"aca va el path de cada uno en su compu" + listPDFs[0]
def convertPDFs(listPDFs):
    listTexts = []
    for i in range(len(listPDFs)):
        text = ''
        with open("C:\\Users\\pc\\Documents\\GitHub\\ProjectFinalAlgo2\\pdfs\\" + listPDFs[i], 'rb') as file:
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

def loadInTrie(): #esta es la funcion que hay que llamar para cargar los archivos al trie
    
    listPDFs = namesPDFs()  #lista de nombres de los pdfs
    listTexts = convertPDFs(listPDFs) #lista de textos de los pdfs como strings
    #limpio todos los textos
    for i in range(len(listPDFs)):
        listTexts[i] = cleanText.cleanText(listTexts[i])

    #creo una lista con los IDs de los pdfs
    idToPdf, pdfToID = pdfFunctions.createPdfID(listPDFs)
    ids = []
    for i in range(len(listPDFs)):
        ids.append(pdfFunctions.getIDFromPdf(listPDFs[i],pdfToID))
        
    #inserto en el trie
    t = trie.Trie()
    for i in range(len(listTexts)):    
        trie.insertMainTrie(t,listTexts[i],ids[i])
    return t

def saveTrie(trie): #esta funcion guarda el trie en un archivo
    with open("trieDocument", "wb") as f:
        pickle.dump(trie, f)
        
def loadTrie(): #esta funcion carga el trie desde un archivo
    with open("trieDocument", "rb") as f:
        trie = pickle.load(f)
    return trie   
      
# T = Trie()
#T = loadInTrie()

#saveTrie(T)
trie.printTrie(loadInTrie().root,1)