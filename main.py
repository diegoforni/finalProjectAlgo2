import load
import rankDocuments
import search
import cleanText

path = input("ingrese la ruta de la carpeta que contiene los PDFs: ")
path = path.replace("\\","\\\\") #cambiamos las barras por doble barra porque sino python no reconoce la ruta

A = load.loadInTrie(path) #cargamos los pdfs en el trie

load.saveTrie(A) #guardamos el trie en un archivo

print("El trie se ha guardado en un archivo llamado trieDocument")

T = load.loadTrie() #cargamos el trie desde el archivo

consulta = input("Ingrese la consulta: ")

consulta = cleanText.cleanText(consulta) #limpiamos la consulta


pdfNames = load.namesPDFs(path)
texts = load.convertPDFs(pdfNames,path) #cargamos los textos de los pdfs
print(rankDocuments.rankDocuments(consulta, texts,T,len(texts),pdfNames)) #rankeamos los documentos