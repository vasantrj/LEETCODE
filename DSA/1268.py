"""
Problem: Search Suggestions System
LeetCode ID: 1268
Pattern: Binary Search / Sorting
Difficulty: Medium
Time Complexity: O(n log n + m log n)
Space Complexity: O(m)

Approach:
1. Sort all products lexicographically so that products with the same
   prefix appear next to each other.
2. Build the search prefix one character at a time.
3. For each prefix, use binary search to find the first product that
   is lexicographically greater than or equal to the prefix.
4. Starting from that position, inspect at most the next three products.
5. Add a product to the suggestions only if it starts with the current
   prefix. Since the products are sorted, once a product does not match,
   later products will not match either.
6. Store the suggestions for every prefix and return the result.
"""

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        result = []
        prefix = ""
        
        for ch in searchWord:
            prefix += ch
            idx = bisect.bisect_left(products, prefix)
            suggestions = []
            for i in range(idx, min(idx + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            
            result.append(suggestions)
        return result
    