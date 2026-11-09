
"""
Problem: H-Index
LeetCode ID: 274
Pattern: Array / Counting Sort / Bucketing
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Let n be the total number of papers.
2. Create a bucket array of size n + 1 to count citation values.
3. For every paper, place its citation count into the bucket
   at min(c, n). Citation counts greater than n are grouped
   into bucket n because the H-index cannot exceed n.
4. Traverse the buckets from n down to 0.
5. Maintain papers as the cumulative number of papers having
   at least the current number of citations.
6. If papers >= h, at least h papers have h or more citations.
7. Return the first valid h, which is the maximum H-index.
"""

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations:
            buckets[min(c, n)] += 1
        papers = 0
        for h in range(n, -1, -1):
            papers += buckets[h]
            if papers >= h:
                return h
        return 0
