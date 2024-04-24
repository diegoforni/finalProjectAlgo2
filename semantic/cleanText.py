from purgeFillers import *
from parseSemantic import *

#complejidad O(n) donde n es la cantidad de palabras en la oración
def cleanText(text): #recibe una cadena de texto y devuelve una lista de palabras
    text = text.lower() #paso el texto a minusculas
    words = text.split() #separo las palabras en una lista
    
    for i in range(len(words)): #limpio el texto de palabras vacias
        words[i] = purgeFillers(words[i])
        
    while None in words: #elimino los none de la lista
        words.remove(None)
    
    for i in range(len(words)): #saco las terminaciones a las palabras
        words[i] = parseSemantic(words[i])

    return words