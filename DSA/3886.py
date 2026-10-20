"""
Problem: Sum of Sortable Integers
LeetCode ID: 3886
Pattern: Arrays / Divisors / Greedy Validation
Difficulty: Medium
Time Complexity: O(n^2)
Space Complexity: O(n)

Approach:
1. Iterate over every possible block size k from 1 to n.
2. Skip k if it does not divide n evenly, since the array must
   be partitioned into equal-sized blocks.
3. For each block, count cyclic descents, including the comparison
   between the last and first elements. A block is sortable under
   cyclic rotation if it has at most one cyclic descent.
4. Verify that the minimum of the current block is at least the
   maximum of the previous block, ensuring the sorted blocks remain
   globally ordered.
5. If every block passes both checks, add k to the answer.
6. Return the sum of all valid block sizes.
"""

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            ok = True
            prev_max = 0
            for s in range(0, n, k):
                blk = nums[s:s + k]
                desc = 0
                for i in range(k):
                    if blk[i] > blk[(i + 1) % k]:
                        desc += 1
                        if desc > 1:
                            break

                if desc > 1 or min(blk) < prev_max:
                    ok = False
                    break
                prev_max = max(blk)

            if ok:
                ans += k
        return ans