import os
import pickle
import vectorizeWordDiego as vwd
import cleanText
import load

def loadOrCreateMatrix(filePath, texts):
    if os.path.exists(filePath):
        with open('matrix', 'rb') as file:
            matrix = pickle.load(file)
        print("Matrix loaded")
    else:
        texts = vwd.splitTexts(texts)
        for text in range(len(texts)):
            texts[text] = cleanText.cleanText(texts[text])
        matrix = vwd.fillMatrix(texts)
        
        with open('matrix', 'wb') as file:
            pickle.dump(matrix, file)
        print("Matrix created")
    
    return matrix

def loadOrCreateTrie(filePath,pdfNames,texts):
    if os.path.exists(filePath):
        with open("trieDocument", "rb") as f:
            trie = pickle.load(f)
        print("Trie loaded")
    else:
        trie = load.loadInTrie(pdfNames,texts)
        
        with open("trieDocument", "wb") as f:
            pickle.dump(trie, f)
        print("Trie created")
    
    return trie