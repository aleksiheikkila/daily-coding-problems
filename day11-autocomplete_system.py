""" Day 11. Medium

Implement an autocomplete system. That is, given a query string s and a set of all possible 
query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], 
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


############

Let's implement a trie and use it.

"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        # is this the ending point (last char) for a word in Trie
        self.is_end = False
        self.children = {}  # char -> TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode("")


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                newNode = TrieNode(c)
                node.children[c] = newNode
            node = node.children[c]
        node.is_end = True


    def insert_list(self, word_list: list) -> None:
        """Add multiple words to the Trie"""
        for word in word_list:
            self.insert(word)


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
            
        return True if node.is_end else False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
            
        return True


    def get_all_with_prefix(self, prefix: str) -> list:
        matches = []

        # go to the right node covering the prefix.
        node = self.root
        for c in prefix:
            if c not in node.children:
                # prefix not in Trie, no matches. Return the empty list
                return matches 
            node = node.children[c]

        # Then collect every word from that point on to the result
        stack = [(node, prefix)]  # [node, string],  DFS
        while stack:
            node, txt = stack.pop()
            if node.is_end:
                matches.append(txt)
            for next_char, node in node.children.items():
                stack.append((node, txt + next_char))

        return matches
        

# TEST CASE
t = Trie()
t.insert_list(["dog", "deer", "deal"])
print(t.get_all_with_prefix("de"))
