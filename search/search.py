
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

def insertMainTrie(t,array,document_id,documentTitle):
    for word in array:
        insertTrieDict(t,word,document_id,documentTitle)




#searches words from the array the TrieDict structure 
def searchTrieDict(T,array): 
    wordsInTrie = {} #store a key-value pair to keep track of the words that are or not in the trie. For example: {apple: False, app: True}
    for word in array: 
        wasFound = searchTrieDictRecursive(T.root,word,word,foundChars ="")
        wordsInTrie[word] = wasFound 
    return wordsInTrie


#Recursive function for searchTrieDict
def searchTrieDictRecursive(current,word,copyWord,foundChars): 
    
    if current is None: 
        return False 
   
    if len(word) < 1: 
        if copyWord != foundChars: 
            return False 
        return current.isEndOfWord 
    

    if current.children is not None: 
        for child in current.children: 
            if child == word[0]: 
                foundChars += child 
                return searchTrieDictRecursive(current.children[child],word[1:],copyWord,foundChars)
        return False 
    

T = Trie()
array = ['apple','app','ape','banana','bat','ball','cat','car','dog']
insertMainTrie(T,array,1,'document1')

array2 = ['apple','app','horse','keyboard','bat','ball','lion','car','truck']

wordsInTrie = searchTrieDict(T,array2)
print(wordsInTrie) 
