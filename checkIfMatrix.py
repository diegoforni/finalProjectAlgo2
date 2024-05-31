import os
import pickle
import vectorizeWordDiego as vwd
import cleanText
import load
import time

def loadOrCreateMatrix(filePath, texts,t,cantTextos):
    if os.path.exists(filePath):
        time1 = time.time()
        with open('matrix', 'rb') as file:
            matrix = pickle.load(file)
        print("Matrix loaded")
        time1 = time.time() - time1
        print("Time to load matrix: ", time1)
    else:
        time1 = time.time()
        texts = vwd.splitTexts(texts)
        for text in range(len(texts)):
            texts[text] = cleanText.cleanText(texts[text])
        matrix = vwd.fillMatrix(texts,t,cantTextos)
        
        with open('matrix', 'wb') as file:
            pickle.dump(matrix, file)
        print("Matrix created")
        time1 = time.time() - time1
        print("Time to create matrix: ", time1)
    return matrix

def loadOrCreateTrie(filePath,pdfNames,texts):
    if os.path.exists(filePath):
        time1 = time.time()
        with open("trieDocument", "rb") as f:
            trie = pickle.load(f)
        print("Trie loaded")
        time1 = time.time() - time1
        print("Time to load trie: ", time1)
    else:
        trie = load.loadInTrie(pdfNames,texts)
        
        with open("trieDocument", "wb") as f:
            pickle.dump(trie, f)
        print("Trie created")
    return trie