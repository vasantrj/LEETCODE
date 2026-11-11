
"""
Problem: Insert Delete GetRandom O(1)
LeetCode ID: 380
Pattern: Hashing / Array / Design
Difficulty: Medium
Time Complexity:
    insert: O(1) average
    remove: O(1) average
    getRandom: O(1)
Space Complexity: O(n)

Approach:
1. Maintain a list named vals to store the elements.
2. Maintain a dictionary named idx to map each value
   to its index in the list.
3. For insert:
   - Check whether the value already exists.
   - If it exists, return False.
   - Otherwise, store its index in the dictionary and
     append it to the list.
4. For remove:
   - Check whether the value exists.
   - Find its index and retrieve the last element.
   - Move the last element into the position being removed.
   - Update the last element's index in the dictionary.
   - Remove the last list element and delete the target
     value from the dictionary.
5. For getRandom:
   - Use random.choice() to select an element uniformly
     from the list.
6. Return the appropriate result for each operation.
"""


import random

class RandomizedSet:
    def __init__(self):
        self.vals = [] 
        self.idx = {}  

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        i = self.idx[val]
        last = self.vals[-1]
        self.vals[i] = last
        self.idx[last] = i
        self.vals.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)