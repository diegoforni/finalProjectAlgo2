class Trie:
    root = None

class TrieNode:
    parent = None
    children = None
    key = None
    document_id = None
    isEndOfWord = False
    appearances = {} 

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

def insertTrieDict(t,word,document_id):
    if t.root is None:
        t.root = TrieNode()
        t.root.children = {}
    current = t.root
    found = False
    for char in word:
        found = False
        
        if char in current.children:
            found = True
            
            current.children[char].document_id = document_id
            current = current.children[char]
        
        if found is False:
            newNode = TrieNode()
            newNode.key = char
            newNode.children = {}
            newNode.parent = current
            current.children[char] = newNode
            current = newNode
            newNode.document_id = document_id
    current.isEndOfWord = True

    if current.isEndOfWord and found:
        if current.document_id in current.appearances:
            current.appearances[current.document_id] += 1
        else:
            current.appearances[current.document_id] = 1

    if current.isEndOfWord and not found:
        current.appearances = {current.document_id: 1}


##Inserting an array full of words into the main trie using insertTrieDict
#O(n) where n is the number of words in the array, and O(n*m) if we also consider the insertTrieDict
#function, where m is the length of longest word and n is the number of words in the array

def insertMainTrie(t,array,document_id):
    for word in array:
        insertTrieDict(t,word,document_id)

'''
##Testing the insert functions
T = Trie()
array1 = ['apple','apple','ape','banana','bat','ball','cat','car','dog']
insertMainTrie(T,array1,1)
array6 = ['apple','ape','banana','bat','ball','cat','car','dog']

insertMainTrie(T,array6,6)

printTrie(T.root,0)

print(T.root.children["a"].children["p"].children["p"].children["l"].children["e"].appearances)
#It will print 2 for the last char of "apple" ("e") as the word appears two times

'''

#searches words from the array the TrieDict structure 
def searchTrieDict(T,array): 
    wordsInTrie = {} #store a key-value pair to keep track of the words that are in the Trie 
    for word in array: 
        wordData = searchTrieDictRecursive(T.root,word,word,foundChars="") #returns a new dict with the word data (appearences on each document)
        wordsInTrie[word] = wordData #add the wordData dict to the wordsInTrie dict
    return wordsInTrie


#Recursive function for searchTrieDict
def searchTrieDictRecursive(current,word,copyWord,foundChars): 
    
    if current is None: 
        return 
   
    if len(word) < 1: 
        if copyWord != foundChars: 
            return None #if the word is not Found return None 
        return current.appearances #Return the dict containing the data of the word 
       

    if current.children is not None: 
        for child in current.children: 
            if child == word[0]: 
                foundChars += child 
                return searchTrieDictRecursive(current.children[child],word[1:],copyWord,foundChars)
        return
    
'''
T = Trie()
array = ['apple','apple','ape','banana','bat','ball','cat','car','dog']
insertMainTrie(T,array,1)

array2 = ['apple','app','horse','keyboard','bat','ball','lion','car','truck']
insertMainTrie(T,array2,2)

wordsInTrie = searchTrieDict(T,array) #Use the searchDict function to search for an array of words 
print(wordsInTrie) 
print("----------") 
print(searchTrieDictRecursive(T.root,"apple","apple","")) #Use the recursive function to look for individual words
'''
