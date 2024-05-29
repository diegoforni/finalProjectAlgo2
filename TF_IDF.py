from trie import searchTrieDict,insertTrieDict,Trie,TrieNode,searchTrieDictRecursive, insertMainTrie
import math 

def calculateTF(word, documentID, wordsInText, T):
    # Search the word in the Trie to get the number of appearances in all documents
    wordAppearances = searchTrieDictRecursive(T.root, word, word, "")
    if wordAppearances and documentID in wordAppearances:
        # Get the number of appearances in a certain document
        t = wordAppearances[documentID]
        return t / wordsInText
    else:
        if wordsInText == 0:
            wordsInText = 1
        return 0
   

def calculateIDF(word,T,documents): 
    #Get the numbers of documents in which the word appears  (n)
    n = searchTrieDictRecursive(T.root,word,word,"")
    
    if n is not None: 
        n = len(n)
        return math.log10(1+ n/documents) #IDF 
    else: 
        return math.log10(1+ 0/documents)


def calculateTEF_IDF(word,documentID,wordsInText,T,documents):

    tf = calculateTF(word,documentID,wordsInText,T)
    idf = calculateIDF(word,T,documents)
    return tf * idf 




'''
T= Trie()
document1 = ["messi","messi","messi","ronaldo","ronaldo","balon"]
insertMainTrie(T,document1,1)

document2 = ["messi","ronaldo","futbol","futbol","futbol"]
insertMainTrie(T,document2,2)

print(calculateTEF_IDF("messi",1,6,T,2)) 
'''









