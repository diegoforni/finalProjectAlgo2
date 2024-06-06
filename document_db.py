import load
import rankDocuments
import searchRank
import cleanText
import pickle
import vectorizeWordDiego as vwd

texts = None




def carga(path):
    A,lengthTexts = load.loadInTrie(path) #cargamos los pdfs en el trie

    load.saveTrie(A) #guardamos el trie en un archivo

    print(" ")
    print("El trie se ha guardado en un archivo llamado trieDocument")


    with open("lengthTexts", "wb") as f:
        pickle.dump(lengthTexts, f)



    pdfNames = load.namesPDFs(path)
    with open("pdfNames", "wb") as f:
        pickle.dump(pdfNames, f)


    texts = load.convertPDFs(pdfNames,path) #cargamos los textos de los pdfs
    texts = vwd.splitTexts(texts)
    for text in range(len(texts)):
        texts[text] = cleanText.cleanText(texts[text])
    matrix = vwd.fillMatrix(texts,A,len(pdfNames))
    with open("matrix", "wb") as f:
        pickle.dump(matrix, f)
    return

def busqueda():
    consulta = "criminal mujer"
    consulta = cleanText.cleanText(consulta) #limpiamos la consulta
    # Buscar en memoria: T, pdfNames, lengthTexts
    with open("lengthTexts", "rb") as f:
        lengthTexts = pickle.load(f)
    with open("pdfNames", "rb") as f:
        pdfNames = pickle.load(f)
    with open("trieDocument", "rb") as f:
        T = pickle.load(f)


    print(rankDocuments.rankDocuments(consulta, texts,T,len(pdfNames),pdfNames,lengthTexts))
    return

busqueda()