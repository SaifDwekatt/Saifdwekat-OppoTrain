class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end_of_word

    def starts_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print("Search 'apple':", trie.search("apple"))
    print("Search 'app':", trie.search("app"))
    print("Starts with 'ap':", trie.starts_with("ap"))
    print("Search 'bat':", trie.search("bat"))
