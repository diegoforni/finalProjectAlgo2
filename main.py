import load
import rankDocuments
import cleanText
import checkIfMatrix
import time

path = input("ingrese la ruta de la carpeta que contiene los PDFs: ")
path = path.replace("\\","\\\\") #cambiamos las barras por doble barra porque sino python no reconoce la ruta

print(" ")
consulta = input("Ingrese la consulta: ")

start_time = time.time()

pdfNames = load.namesPDFs(path)
texts = load.convertPDFs(pdfNames,path)

#A,texts,pdfNames = load.loadInTrie(path) #cargamos los pdfs en el trie

T = checkIfMatrix.loadOrCreateTrie("trieDocument",pdfNames,texts)


#load.saveTrie(A) #guardamos el trie en un archivo

#print(" ")
#print("El trie se ha guardado en un archivo llamado trieDocument")

#T = load.loadTrie() #cargamos el trie desde el archivo

consulta = cleanText.cleanText(consulta) #limpiamos la consulta

matrix = checkIfMatrix.loadOrCreateMatrix("matrix",texts,T,len(pdfNames))
print(" ")
print(rankDocuments.getClosest(consulta,T,len(texts),pdfNames,matrix)) #rankeamos los documentos

end_time = time.time()
execution_time = end_time - start_time
print(f"El tiempo de ejecución del algoritmo fue de {execution_time} segundos.")