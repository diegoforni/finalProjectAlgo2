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
    if word in matrix:
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
