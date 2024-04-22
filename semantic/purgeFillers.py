#listado de palabras que no aportan significado a una oración
emptyWords = {
    #Palabras determinantes y pronombres
    "el","la","los","las","un","una","unos","unas","tú","nosotros","ellos","ellas",
    "mi","este", "ese", "aquel", "esta", "esa", "aquella","tu","su","que"
    #adverbios
    "muy","realmente","extremadamente","totalmente","bastante",
    "verdaderamente","plenamente","completamente","absolutamente",
    #preposiciones
    "a","de","en",
    #conjunciones
    "y","o","e","pero","etc","etcétera"
    #sustantivos
    "cosa","asunto","cuestión","ninguno","varios","aquel",
    #simbolos (estan incluidos porque pueden estar solos y considerarse una palabra)
    ".",";",",","(",")","¿","?","¡","!"
}

#ORDEN DE COMPLEJIDAD O(1) ya que la busqueda de un elemento en un conjunto es O(1) 
#porque python usa tablas de hash
#revisa que la palabra este en el listado de palabras vacias 
def purgeFillers(word):
    word = cleanSimbols(word)
    if word in emptyWords:
        return None
    else:
        return word

#limpia las palabras sacandole los simbolos 
def cleanSimbols(word):
    simbols = {".",";",","," ","(",")","¿","?","¡","!"}
    for i in simbols:
        word = word.replace(i,'')
    return word
            

