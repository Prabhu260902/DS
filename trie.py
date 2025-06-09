# cook your dish here
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, name):
        node = self.root
        for ch in str(name):
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        
    def search(self, word, check_end = True):
        node = self.root
        for ch in str(word):
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        else:
            return (True if node.is_end else False) if check_end else True
        
    def startsWith(self, prefix):
        return self.search(prefix, False)
        
    def print_trie(self, node = None, prefix = ""):
        if node is None:
            node = self.root
        if node.is_end:
            print(prefix)
        for ch in node.children.keys():
            self.print_trie(node.children[ch], prefix+ch)
        
words_array = list(map(str,input().split()))
trie = Trie()
for word in words_array:
    trie.insert(word)

trie.print_trie()
find_word = input()
print(trie.search(find_word))# cook your dish here
print(trie.startsWith(find_word))