def loadDictionary(filePath):
    with open(filePath, 'r') as file:
        return [line.strip() for line in file]

def wagnerFischer(s1, s2):
    lenS1, lenS2 = len(s1), len(s2)
    if lenS1 > lenS2:
        s1, s2 = s2, s1
        lenS1, lenS2 = lenS2, lenS1

    currentRow = range(lenS1 + 1)
    for i in range(1, lenS2 + 1):
        previousRow, currentRow = currentRow, [i] + [0] * lenS1
        for j in range(1, lenS1 + 1):
            add, delete, change = previousRow[j] + 1, currentRow[j-1] + 1, previousRow[j-1]
            if s1[j-1] != s2[i-1]:
                change += 1
            currentRow[j] = min(add, delete, change)

    return currentRow[lenS1]

def spellCheck(word):
    dictionary = loadDictionary("spanishWords.txt")

    closestWord = None
    closestDistance = float('inf')
    
    for correctWord in dictionary:
        distance = wagnerFischer(word, correctWord)
        if distance == 0:
            return None
        elif distance == 1:
            return correctWord
        elif distance < closestDistance:
            closestDistance = distance
            closestWord = correctWord
    
    if closestDistance == 2:
        return closestWord
    
    return None
