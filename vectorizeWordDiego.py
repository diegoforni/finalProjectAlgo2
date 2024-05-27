import cleanText 
import load

##Cargar su path con los pdfs antes de usar
path = 'C:\\Users\\juana\\OneDrive\\Documents\\GitHub\\ProjectFinalAlgo2\\pdfs'

pdfNames = load.namesPDFs(path)

texts = load.convertPDFs(pdfNames, path)

def splitTexts(texts):
    paragraphs = []

    for text in texts:
        text_paragraphs = text.split("\n")
        
        paragraphs.extend(text_paragraphs)

    return paragraphs

def calculate_tf(text, word):
    words = text
    word_count = words.count(word)
    return word_count / len(words) if len(words) > 0 else 0

def fillMatrix(texts):
    matrix = {}
    allWords = set()
    
    for text in texts:
        allWords.update(text)
    
    for word in allWords:
        matrix[word] = []
        for text in texts:
            wordTF = calculate_tf(text, word)
            matrix[word].append(wordTF)
    
    return matrix

def printMatrix(matrix):
    for word, tf_scores in matrix.items():
        print(word, tf_scores)

##Chequea si word existe en alguna fila de la matriz
def existInMatrix(matrix, word):
    varToCall = cleanText.cleanText(word)[0]
    if varToCall in matrix:
        return True
    else:
        return False

def calculateDistance(v1, v2):
    distance = 0
    for i in range(len(v1)):
        distance += (v1[i] - v2[i])**2
    return distance**0.5


def getClosestWords(matrix, v1):
    # Inicializar lista con distancias grandes y palabras vacías
    closestWords = [(float('inf'), ''), (float('inf'), ''), (float('inf'), '')]
    v1 = matrix[v1]
    for key, vector in matrix.items():
        distance = calculateDistance(v1, vector)
        if distance != 0:
            if distance < closestWords[0][0]:
                closestWords = [(distance, key)] + closestWords[:2]
            elif distance < closestWords[1][0]:
                closestWords = [closestWords[0]] + [(distance, key)] + [closestWords[1]]
            elif distance < closestWords[2][0]:
                closestWords[2] = (distance, key)
    
    # Extraer solo las palabras
    return [word for dist, word in closestWords]


#start_time = time.time()
texts = splitTexts(texts)
for text in range(len(texts)):
    texts[text] = cleanText.cleanText(texts[text])
    
#print(texts[0])
matrix = fillMatrix(texts)
if existInMatrix(matrix, "póker"):
    varToCall = cleanText.cleanText("póker")[0]
    #print(getClosestWords(matrix, varToCall))
    
#printMatrix(matrix)
#print('cantidad de palabras: ', len(matrix))
#print('cantidad de parrafos: ', len(matrix['hispana']))
#print(texts)
#print(matrix[closest[1]])
#print(v1)
#end_time = time.time()
#execution_time = end_time - start_time
#print("Time to execute getClosestWords: ", execution_time, " seconds")