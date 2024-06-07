import trie as tr
import pickle
import time

##Cargar su path con los pdfs antes de usar

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

def fillMatrix(texts,t,cantTextos):
    matrix = {}
    allWords = set()
    
    for text in texts:
        allWords.update(text)
    
    for word in allWords:
        matrix[word] = []
        sumVec = 0
        for text in texts:
            wordTF = calculate_tf(text, word)
            matrix[word].append(wordTF)
        wordOccurrence = tr.searchTrieDictRecursive(t.root, word, word, foundChars="")
        for i in range(cantTextos):
            if i in wordOccurrence:
                matrix[word].append(1)
                sumVec += 1
            else:
                matrix[word].append(0)
        if sumVec < cantTextos/2:
            matrix[word].append(1)
        else:
            matrix[word].append(0)

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
    return distance**0.5,True


def getClosestWords(matrix, v1):
    # Inicializar lista con distancias grandes y palabras vacías
    closestWords = [(float('inf'), ''), (float('inf'), ''), (float('inf'), '')]
    v1Vec = matrix[v1]
    time1 = time.time()
    
    with open("pdfNames", "rb") as f:
        pdfNames = pickle.load(f)
    cantTextos = len(pdfNames)
    cantParrafos = len(v1Vec)
    for key, vector in matrix.items():
        
        found = False
        if vector[-1] == 1:
            for i in range(cantParrafos - cantTextos, cantParrafos):
                if v1Vec[i] == 1 and vector[i] == 1:
                    distance,found = calculateDistance(v1Vec, vector)
                    break
                
        if found and distance != 0:
            if distance < closestWords[0][0]:
                closestWords = [(distance, key)] + closestWords[:2]
            elif distance < closestWords[1][0]:
                closestWords = [closestWords[0]] + [(distance, key)] + [closestWords[1]]
            elif distance < closestWords[2][0]:
                closestWords[2] = (distance, key)
                
    time1 = time.time() - time1
    print("Time to calculate distances: ", time1)
    
    # Extract only the words
    return [word for dist, word in closestWords if word != '']
