
"""
Problem: Implement Trie (Prefix Tree)
LeetCode ID: 208
Pattern: Trie / Prefix Tree
Difficulty: Medium
Time Complexity: O(L) per operation, where L is the input length
Space Complexity: O(N * L) worst case for N inserted words of length L

Approach:
1. Define TrieNode with a dictionary of children and an is_end flag.
2. Initialize the Trie with an empty root node.
3. For insert(), traverse each character and create a child node
   whenever the character does not already exist.
4. Mark the final node as the end of the inserted word.
5. Implement _find() to traverse a word or prefix and return the
   matching node, or None if the path does not exist.
6. Implement search() by checking whether the complete word exists
   and its final node is marked as a word ending.
7. Implement startsWith() by checking whether the prefix path exists.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def _find(self, s: str):
        node = self.root

        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None

        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

