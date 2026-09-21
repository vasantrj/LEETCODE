"""
Problem: Find X Value of Array I
LeetCode ID: 3524
Pattern: Dynamic Programming / Modular Arithmetic
Difficulty: Medium
Time Complexity: O(n * k)
Space Complexity: O(k)

Approach:
1. We need to count subarrays based on the remainder of their product
   when divided by k.
2. Maintain cnt[r] as the number of subarrays ending at the previous
   position whose product has remainder r modulo k.
3. For each number num, calculate its remainder:
   a = num % k.
4. Create a new array to represent subarrays ending at the current
   position:
   - Every previous subarray with product remainder r can be extended
     with num, producing remainder (r * a) % k.
   - The single-element subarray [num] has remainder a.
5. Replace cnt with the newly calculated counts.
6. Add the counts of all subarrays ending at the current position to
   ans, where ans[r] represents the total number of subarrays whose
   product has remainder r.
7. Return ans after processing every element.
"""

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        cnt = [0] * k 

        for num in nums:
            a = num % k
            new = [0] * k
            for r in range(k):
                if cnt[r]:
                    new[(r * a) % k] += cnt[r]
            new[a] += 1 
            cnt = new
            for r in range(k):
                ans[r] += cnt[r]

        return ans