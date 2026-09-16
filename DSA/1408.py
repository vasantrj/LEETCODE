"""
Problem: String Matching in an Array
LeetCode ID: 1408
Pattern: String Matching
Difficulty: Easy
Time Complexity: O(n^2 * m)
Space Complexity: O(n)

Approach:
1. Iterate through every word in the words array.
2. For each word w, compare it with every other word in the array.
3. Check whether w is a substring of another word:
   - w must be different from the other word.
   - w in other checks whether w occurs inside the other word.
4. If w is found as a substring of at least one other word, include it
   in the result.
5. Use any() to stop checking other words as soon as a match is found.
6. Return the list of all words that are substrings of another word.
"""


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [w for i, w in enumerate(words)
                if any(w != other and w in other for j, other in enumerate(words) if i != j)]