class TrieNode:
    def __init__(self, string="", is_word=False):
        self.string=""
        self.is_word = False
        self.adjacency_list = {}
    
    def add_word(self, word):
        startnode = self
        for i, letter in enumerate(word):
            if letter in startnode.adjacency_list:
                startnode = startnode.adjacency_list[letter]
            else:
                startnode.adjacency_list[letter] = TrieNode()
                startnode = startnode.adjacency_list[letter]
            startnode.string = word[:i+1]
        startnode.is_word = True
    

class Trie:
    def __init__(self, wordlist=[]):
        self.root = TrieNode()
        for word in wordlist:
            self.root.add_word(word)
    def add_word(self, word):
        self.root.add_word(word)

    def insert(self, word):
        self.add_word(word) 
        
    def is_word(self, word):
        current_node = self.root
        is_word = False
        for letter in word:
            if letter not in current_node.adjacency_list:
                return False
            current_node = current_node.adjacency_list[letter]
        return current_node.is_word

    def is_prefix(self, prefix):
        current_node = self.root
        for letter in prefix:
            if letter not in current_node.adjacency_list:
                return False
            current_node = current_node.adjacency_list[letter]
        return True
