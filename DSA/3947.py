"""
Problem: Maximum Number of Items From Sale II
LeetCode ID: 3947
Pattern: Greedy / Sorting / Harmonic Sum
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Item i can trigger a free copy of every other item j whose factor is a
   multiple of factor_i. Let g_i be the number of such items. Only the first
   g_i purchased copies of item i are worth 2 (1 bought + 1 free); any
   further copy is worth 1.
2. Count items per factor, then use a harmonic sum over multiples to get
   g_i for every factor in O(n log n).
3. Every "value 1" copy should be bought from the cheapest item (price mn).
4. Taking one more "value 2" copy at price p displaces at most ceil(p / mn)
   cheap copies, so it helps only when p <= 2 * mn.
5. Sort candidates by price and take value-2 copies greedily while the
   price is <= 2 * mn and affordable. Spend the leftover budget on cheapest
   copies.
6. Answer = 2 * (value-2 copies bought) + leftover // mn.
"""

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        for f, _ in items:
            cnt[f] += 1

        # multiples[f] = number of items whose factor is a multiple of f
        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            multiples[f] = sum(cnt[k] for k in range(f, n + 1, f))

        mn = min(p for _, p in items)

        # (price, number of value-2 copies available) for each item
        cand = []
        for f, p in items:
            g = multiples[f] - 1  # exclude itself
            if g > 0 and p <= 2 * mn:
                cand.append((p, g))
        cand.sort()

        rem = budget
        a = 0
        for p, g in cand:
            k = min(g, rem // p)
            a += k
            rem -= k * p
            if k < g:  # can't afford more; later items cost >= p
                break

        return 2 * a + rem // mn