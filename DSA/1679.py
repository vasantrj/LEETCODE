"""
Problem: Max Number of K-Sum Pairs
LeetCode ID: 1679
Pattern: Hash Map / Two Sum
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a hash map to store the frequency of numbers that have not
   yet been paired.
2. For each number n, calculate its required complement:
   complement = k - n.
3. If the complement is available in the hash map:
   - Use one occurrence of the complement to form a valid pair.
   - Decrease its frequency by one.
   - Increment the number of operations.
4. If the complement is not available, store the current number in
   the hash map for a future number to pair with.
5. Each number is processed exactly once, giving an O(n) solution
   without sorting the array.
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        operations = 0
        for num in nums:
            complement = k - num
            if seen[complement] > 0:
                seen[complement] -= 1
                operations += 1
            else:
                seen[num] += 1
        return operations