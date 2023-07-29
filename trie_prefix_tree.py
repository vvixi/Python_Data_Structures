# Trie or Prefix Tree in Python 3.11 by vvixi
class Node:

    def __init__(self, val: str):

        self.val = val
        self.isWord = False
        self.children = {}

    def __repr__(self):

        return f'\nNode: {self.val}'

class PrefixTree:

    def __init__(self):
        self.root = Node("*")

    def insert(self, word: str):
        '''
        '''
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if not char in node.children:
                node.children[char] = Node(char)
                print(f'node added: {char}')
            node = node.children[char]
        node.isWord = True    

    def search(self, word: str):
        #idx = 0 
        node = self.root
        for char in word:
            # letter is not in children
            if char not in node.children:
                print(f'\nNode: {char} was not found...')
                return False 
            
            # letter is in children
            elif char in node.children:
                # current node's children is empty and we have more letters in seach word
                node = node.children[char]
        
        if node.isWord:
            return True

        else:
            return False

    def findWord(self, node: Node, word: str):
        if node.isWord:
            print(word)
        for key, val in node.children.items():
            self.findWord(val, word + key)

    def prefixSearch(self, key):
        node = self.root
        for char in key:
            if not node.children.get(char):
                return
            node = node.children[char]

        self.findWord(node, key)
        return

pt = PrefixTree()
pt.insert("mech")
pt.insert("mechanism")
pt.insert("mechanical")
pt.insert("machinations")
print(pt.search("mechanism"))
print(pt.search("mech"))
print(pt.search("meich"))
print(pt.prefixSearch('m'))
