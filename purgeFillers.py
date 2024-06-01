#listado de palabras que no aportan significado a una oración
emptyWords = {
    # Palabras determinantes y pronombres
    "el", "la", "los", "las", "un", "una", "unos", "unas", "tú", "nosotros", "nosotras", "vosotros", "vosotras", "ellos", "ellas",
    "mi", "mis", "tu", "tus", "su", "sus", "nuestro", "nuestra", "nuestros", "nuestras", "vuestro", "vuestra", "vuestros", "vuestras",
    "este", "esta", "estos", "estas", "ese", "esa", "eso", "esos", "esas", "aquel", "aquella", "aquello", "aquellos", "aquellas",
    "esto", "eso", "aquello", "algo", "alguien", "alguno", "alguna", "algunos", "algunas", "cualquier", "cualquiera", "cualesquiera",
    "ningún", "ninguna", "ningunos", "ningunas", "ningún", "ninguna", "ningunos", "ningunas", "todo", "toda", "todos", "todas",
    "mucho", "muchos", "muchas", "poco", "poca", "pocos", "pocas", "varios", "varias", "otro", "otra", "otros", "otras",
    "mío", "mía", "míos", "mías", "tuyo", "tuya", "tuyos", "tuyas", "suyo", "suya", "suyos", "suyas", "nuestro", "nuestra",
    "nuestros", "nuestras", "vuestro", "vuestra", "vuestros", "vuestras", "cuyo", "cuya", "cuyos", "cuyas", "qué", "quién",
    "quienes", "cuál", "cuáles", "cuánto", "cuántos", "cuánta", "cuántas", "cuándo", "dónde", "cómo", "cuánto", "cuántos",
    "cuánta", "cuántas", "cuánto", "cuántos", "cuánta", "cuántas", "cuánto", "cuántos", "cuánta", "cuántas", "cuánto",
    # Verbos
    "ser", "es","siendo", "son", "fue", "fueron", "estar", "está", "estás", "estáis", "están", "estuve", "estuviste", "estuvo", "estuvimos",
    "estuvisteis", "estuvieron", "haber", "he", "has", "ha", "hemos", "habéis", "han", "había", "habías", "habíamos", "habíais",
    "habían", "hube", "hubiste", "hubo", "hubimos", "hubisteis", "hubieron", "habré", "habrás", "habrá", "habremos", "habréis",
    "habrán", "habría", "habrías", "habríamos", "habríais", "habrían", "haya", "hayas", "hayamos", "hayáis", "hayan", "hubiera",
    "hubieras", "hubiéramos", "hubierais", "hubieran", "hubiese", "hubieses", "hubiésemos", "hubieseis", "hubiesen", "hayan",
    "pueden", "puede", "puedo", "podemos", "podéis", "puedes", "pueden", "podría", "podrías", "podríamos", "podríais", "podrían",
    # Adverbios
    "muy", "realmente", "extremadamente", "totalmente", "bastante",
    "verdaderamente", "plenamente", "completamente", "absolutamente", "sí", "no", "quizás", "talvez", "acaso",
    # Preposiciones
    "a", "ante", "bajo", "cabe", "con", "contra", "de","del", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante",
    "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "vía",
    # Conjunciones
    "y", "e", "ni", "o", "u", "pero", "sino", "sinoque", "mientras", "aunque", "aun", "aún", "sin embargo", "no obstante",
    "por tanto", "por consiguiente", "luego", "así que", "así pues", "ya que", "puesto que", "porque", "pues", "que", "como",
    "cuando", "donde", "cómo", "que", "porque", "pues", "para que", "a fin de que", "con tal de que", "siempre que", "en caso de que",
    "aunque", "aun cuando", "si", "sí", "no", "tal como", "así como", "igual que", "tan pronto como", "tanto como",
    "tambien", "también", "además", "asimismo", "incluso", "hasta", "incluso", "inclusive", "ni siquiera", "ni tan siquiera",
    # Sustantivos
    "cosa", "cosas", "asunto", "asuntos", "cuestión", "cuestiones", "ninguno", "ninguna", "ningunos", "ningunas", "varios",
    "varias", "aquel", "aquellos", "aquella", "aquellas", "esto", "eso", "aquello", "algo", "alguien", "nadie", "cualquier",
    "cualquiera", "cualesquiera", "ningún", "ninguno", "ninguna", "mucho", "muchos", "mucha", "muchas", "poco", "pocos",
    "poca", "pocas", "todo", "toda", "todos", "todas", "algo", "alguien", "nada", "nadie", "otro", "otra", "otros", "otras",
    "más", "menos", "mucho", "poco", "varios", "varias", "cada", "cual", "cuales", "cuando", "quien", "quienes", "cuyo", "cuya",
    "cuyos", "cuyas", "qué", "cuál", "cuáles", "cuánto", "cuánta", "cuántos", "cuántas", "dónde", "adónde", "cuándo", "cómo",
    "de qué", "con qué", "a qué", "por qué", "para qué", "cuál", "cuáles", "cuánto", "cuánta", "cuántos", "cuántas", "cuándo",
    "dónde", "cómo", "por qué", "para qué",
    # Simbolos
    ".", ";", ",", ":", "(", ")", "[", "]", "{", "}", "?", "¿", "!", "¡", "-", "'", '"', "/", "\\", "*", "&", "@", "#", "$", "%", "^", "=", "+", "~", "<", ">", "|","*","_","`","¨","´","°","¬"
}

def removeAccents(word):
    accents  = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u'}
    return ''.join(accents.get(c, c) for c in word) 
#ORDEN DE COMPLEJIDAD O(1) ya que la busqueda de un elemento en un conjunto es O(1) 
#porque python usa tablas de hash
#revisa que la palabra este en el listado de palabras vacias 
def purgeFillers(word):
    word = cleanSimbols(word)
    word = removeAccents(word)
    if word in emptyWords:
        return None
    else:
        return word

#limpia las palabras sacandole los simbolos 
def cleanSimbols(word):
    simbols = {".", ";", ",", ":", "(", ")", "[", "]", "{", "}", "?", "¿", "!", "¡", "-", "'", '"', "/", "\\", "*", "&", "@", "#", "$", "%", "^", "=", "+", "~", "<", ">", "|","*","_","`","¨","´","°","¬"}
    for i in simbols:
        word = word.replace(i,'')
    return word
            
