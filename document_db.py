import sys
import load
import rankDocuments
import cleanText
import pickle
import vectorizeWordDiego as vwd
import spellCheck

texts = None

def carga(path):
    A, lengthTexts = load.loadInTrie(path)  # cargamos los pdfs en el trie

    load.saveTrie(A)  # guardamos el trie en un archivo

    with open("lengthTexts", "wb") as f:
        pickle.dump(lengthTexts, f)

    pdfNames = load.namesPDFs(path)
    with open("pdfNames", "wb") as f:
        pickle.dump(pdfNames, f)

    texts = load.convertPDFs(pdfNames, path)  # cargamos los textos de los pdfs
    texts = vwd.splitTexts(texts)
    for text in range(len(texts)):
        texts[text] = cleanText.cleanText(texts[text])
    matrix = vwd.fillMatrix(texts, A, len(pdfNames))
    with open("matrix", "wb") as f:
        pickle.dump(matrix, f)

    print("document data-base created successfully")
    return

def busqueda(query):
    query_words = query.split()
    for word in query_words:
        spellChecked = spellCheck.spellCheck(word)
        if spellChecked is not None:
            query_words.append(spellChecked)
            
    query = cleanText.cleanText(' '.join(query_words))  # limpiamos la consulta

    # Buscar en memoria: T, pdfNames, lengthTexts, texts
    with open("lengthTexts", "rb") as f:
        lengthTexts = pickle.load(f)
    with open("pdfNames", "rb") as f:
        pdfNames = pickle.load(f)
    with open("trieDocument", "rb") as f:
        T = pickle.load(f)
    with open("matrix", "rb") as f:
        matrix = pickle.load(f)
    
    result = rankDocuments.rankDocuments(query, texts, T, len(pdfNames), pdfNames, lengthTexts)
    if result == 'Document not found':
        print('Document not found')
        return
    for i in range(len(result)):
        print(i + 1,")", result[i])
    return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 document_db.py -create <local_path> ")
        sys.exit(1)

    command = sys.argv[1]

    if command == "-create":
        if len(sys.argv) != 3:
            print("Uso: python document_db.py -create <local_path>")
            sys.exit(1)
        local_path = sys.argv[2]
        carga(local_path)
    elif command == "-search":
        if len(sys.argv) != 3:
            print("Uso: python document_db.py -search <text>")
            sys.exit(1)
        query = sys.argv[2]
        busqueda(query)
    else:
        print("Comando no reconocido. Uso: python document_db.py -create <local_path> | -search <text>")
        sys.exit(1)
