from trie import * 
from pdfFunctions import *
import pickle
import os 
import sys
sys.path.append("C:\\Users\\Facultad Juli\\Documents\\GitHub\\finalProjectAlgo2\\dataStructure")    

from semantic.cleanText import cleanText

#Acá va la función que recibe una lista de pdf para insertar en el Trie 

#recibo una lista de pdfs y los inserto en el trie
def namesPDFs():
    listPDFs = []
    listPDFs = os.listdir("C:\\Users\\Facultad Juli\\Documents\\GitHub\\finalProjectAlgo2\\pdfs")
    return listPDFs
    
#def convertPDFs(listPDFs):
   
cadenaText = "abdjaks -- asd asadd" 
print(cleanText(cadenaText))