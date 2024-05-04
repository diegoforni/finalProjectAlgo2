from trie import searchTrieDict,insertTrieDict,Trie,TrieNode,searchTrieDictRecursive, insertMainTrie
import math 

def calculateTF(word,documentID,wordsInText,T):  

    #Search the word in the Trie to get the number of appearences in the document 
    wordAppearances = searchTrieDictRecursive(T.root,word,word,"") 

    #Get the number of appearences in a certain document 
    t = wordAppearances[documentID] 

    return 1 + math.log10(t/wordsInText) #TF 


def calculateIDF(word,T,documents): 
    #Get the numbers of documents in which the word appears  (n)
    n = len(searchTrieDictRecursive(T.root,word,word,""))

    return math.log10(1+ n/documents) #IDF 


def calculateTEF_IDF(word,documentID,wordsInText,T,documents):

    tf = calculateTF(word,documentID,wordsInText,T)
    idf = calculateIDF(word,T,documents)
    return tf * idf 


def countWordsInText(text):
    words = text.split() 
    return len(words)

'''
T= Trie()
document1 = ["messi","messi","messi","ronaldo","ronaldo","balon"]
insertMainTrie(T,document1,1)

document2 = ["messi","ronaldo","futbol","futbol","futbol"]
insertMainTrie(T,document2,2)

print(calculateTEF_IDF("messi",1,6,T,2)) 
'''









