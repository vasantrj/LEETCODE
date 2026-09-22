"""
Problem: Find X Value of Array II
LeetCode ID: 3525
Pattern: Segment Tree / Modular Arithmetic / Range Queries
Difficulty: Hard
Time Complexity: O((n + q) * k² * log n)
Space Complexity: O(n * k²)

Approach:
1. Each array value only matters through its remainder modulo k.
2. Represent every segment using two pieces of information:
   - f[r]: the product remainder obtained when a segment is appended
     to a prefix whose current remainder is r.
   - cnt[a][b]: the number of non-empty subarrays in the segment whose
     product changes a starting remainder a into a final remainder b.
3. Build a leaf node for every possible value remainder. Since there
   are at most k distinct remainders, cache these leaf representations.
4. Merge two adjacent segments:
   - The transformation function of the combined segment is obtained
     by applying the right segment after the left segment.
   - Count subarrays contained entirely in the left segment.
   - Count subarrays contained entirely in the right segment.
   - Count subarrays crossing the boundary by combining the relevant
     transformations.
5. Store these segment representations in a segment tree so that an
   array update and a range query can both be handled efficiently.
6. For every query:
   - Update the specified array index.
   - Query the range [start, n - 1].
   - Starting with remainder 1, look up the number of subarrays whose
     final product remainder is x.
7. The segment tree avoids rebuilding the entire array after every
   update and allows each query to be answered using only O(log n)
   segment merges.
"""

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        K = k
        rangeK = range(K)

        def leaf(r):
            f = tuple((a * r) % K for a in rangeK)
            cnt = [0] * (K * K)
            for a in rangeK:
                cnt[a * K + f[a]] = 1
            return (f, tuple(cnt))

        leaf_cache = [leaf(r) for r in rangeK]  # at most 5 distinct leaves

        def merge(left, right):
            fl, cl = left
            fr, cr = right
            f = tuple(fr[fl[a]] for a in rangeK)
            cnt = [0] * (K * K)
            for a in rangeK:
                la = fl[a]
                base_l = a * K
                base_r = la * K
                for x in rangeK:
                    cnt[base_l + x] = cl[base_l + x] + cr[base_r + x]
            return (f, tuple(cnt))

        size = 1
        while size < n:
            size <<= 1
        if size == 0:
            size = 1

        id_f = tuple(rangeK)
        id_cnt = tuple([0] * (K * K))
        identity_node = (id_f, id_cnt)  # padding for indices >= n, never actually queried

        tree = [identity_node] * (2 * size)
        for i in range(n):
            tree[size + i] = leaf_cache[nums[i] % K]
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(idx, val):
            i = size + idx
            tree[i] = leaf_cache[val % K]
            i >>= 1
            while i >= 1:
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
                i >>= 1

        def query(l, r):  # inclusive, 0-indexed
            l += size
            r += size + 1
            left_parts = []
            right_parts = []
            while l < r:
                if l & 1:
                    left_parts.append(tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    right_parts.append(tree[r])
                l >>= 1
                r >>= 1
            parts = left_parts + right_parts[::-1]
            result = parts[0]
            for p in parts[1:]:
                result = merge(result, p)
            return result

        result = []
        start_res = 1 % K
        n1 = n - 1
        for index, value, start, x in queries:
            update(index, value)
            f, cnt = query(start, n1)
            result.append(cnt[start_res * K + x])
        return result