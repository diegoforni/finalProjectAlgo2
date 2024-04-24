class Trie:
    root = None

class TrieNode:
    parent = None
    children = None
    key = None
    document_id = None
    isEndOfWord = False

def printTrie(node, level):
    if node is None:
        return
    if node.key is not None:
        print(' ' * level + node.key)
    if node.children:
        for child_key, child_node in node.children.items():
            printTrie(child_node, level + 1)

##Inserting a word into the trie using python dictionaries
#O(n) where n is the length of the word
#t is the trie, word is the word to be inserted, and document_id is the document_id of the document containing the word
#documentTitle is the title of the document containing the word


def createPdfID(pdfNamesList):
    pdfToID = {}
    idToPdf = {}
    i = 0
    for pdfName in pdfNamesList:
        pdfToID[i] = pdfName
        idToPdf[pdfName] = i
        i += 1
    return pdfToID, idToPdf

def getPdfFromID(id, idToPdf):
    return idToPdf[id]


def getIDFromPdf(pdf, pdfToID):

    return pdfToID[pdf]

pdfList = ['apple','app','ape','banana','bat','ball','cat','car','dog']

idToPdf, pdfToID = createPdfID(pdfList)

print(getPdfFromID(5,idToPdf))
print(getIDFromPdf('banana',pdfToID))


def insertTrieDict(t,word,document_id,documentTitle):
    if t.root is None:
        t.root = TrieNode()
        t.root.children = {}
    current = t.root
    
    for char in word:
        found = False
        
        if char in current.children:
            found = True
            if not(document_id in current.children[char].document_id):
                current.children[char].document_id[document_id] = documentTitle
            current = current.children[char]
        
        if found is False:
            newNode = TrieNode()
            newNode.key = char
            newNode.children = {}
            newNode.parent = current
            current.children[char] = newNode
            current = newNode
            newNode.document_id = {document_id:documentTitle}
    current.isEndOfWord = True

##Inserting an array full of words into the main trie using insertTrieDict
#O(n) where n is the number of words in the array, and O(n*m) if we also consider the insertTrieDict
#function, where m is the length of longest word and n is the number of words in the array

def insertMainTrie(t,array,document_id,documentTitle):
    for word in array:
        insertTrieDict(t,word,document_id,documentTitle)


##Testing the insert functions
t = Trie()
array = ['apple','app','ape','banana','bat','ball','cat','car','dog']
insertMainTrie(t,array,1,'document1')

printTrie(t.root,0)

