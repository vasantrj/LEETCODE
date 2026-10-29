"""
Problem: Palindromic Path Queries in a Tree
LeetCode ID: 3841
Pattern: Tree / LCA + Euler Tour + Fenwick Tree (BIT) + Bitmask Parity
Difficulty: Hard
Time Complexity: O(n log n + q log n)
Space Complexity: O(n log n)

Approach:
1. A path's characters can be rearranged into a palindrome iff at most one
   letter occurs an odd number of times. Track letter parity as a 26-bit mask,
   so the check is m & (m - 1) == 0.
2. Root the tree at 0. Let P[v] = XOR of single-letter bits on the root-to-v
   path (inclusive). Compute it with an iterative DFS that also records
   tin/tout (Euler tour) and depth.
3. Build a binary lifting table up[j][v] so that LCA(u, v) is found in O(log n).
4. Path mask for u-v = P[u] ^ P[v] ^ bit(char[lca]). The LCA's letter cancels
   in P[u] ^ P[v], so we XOR it back in once.
5. Updates change a node's letter, which flips the mask for its entire subtree.
   That is a range XOR over [tin[u], tout[u]] and a point query at tin[v], so
   use a Fenwick tree over XOR:
   - update: add(tin[u], d) and add(tout[u] + 1, d), where
     d = bit(old) ^ bit(new).
   - point query: pref(tin[v]) gives the accumulated XOR at v.
6. The true root-to-v mask is path_val(v) = P[v] ^ pref(tin[v]).
7. For each query, an update modifies the BIT (skipped if the letter is
   unchanged), and a query computes the path mask and checks the
   at-most-one-odd-bit condition.
"""


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        LOG = max(1, (n - 1).bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        P = [0] * n
        chars = [ord(c) - 97 for c in s]
        timer = 0
        P[0] = 1 << chars[0]
        stack = [(0, -1, 0)]
        up[0][0] = 0
        while stack:
            v, par, state = stack.pop()
            if state == 0:
                tin[v] = timer
                timer += 1
                stack.append((v, par, 1))
                for w in adj[v]:
                    if w != par:
                        up[0][w] = v
                        depth[w] = depth[v] + 1
                        P[w] = P[v] ^ (1 << chars[w])
                        stack.append((w, v, 0))
            else:
                tout[v] = timer - 1

        for j in range(1, LOG):
            prev, cur = up[j - 1], up[j]
            for v in range(n):
                cur[v] = prev[prev[v]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for j in range(LOG):
                if diff >> j & 1:
                    a = up[j][a]
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return up[0][a]

        bit = [0] * (n + 2)

        def add(i: int, d: int) -> None:
            i += 1
            while i <= n + 1:
                bit[i] ^= d
                i += i & -i

        def pref(i: int) -> int:
            i += 1
            r = 0
            while i > 0:
                r ^= bit[i]
                i -= i & -i
            return r

        def path_val(v: int) -> int:
            return P[v] ^ pref(tin[v])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = ord(parts[2]) - 97
                if c != chars[u]:
                    d = (1 << chars[u]) ^ (1 << c)
                    chars[u] = c
                    add(tin[u], d)
                    add(tout[u] + 1, d)
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                m = path_val(u) ^ path_val(v) ^ (1 << chars[l])
                ans.append(m & (m - 1) == 0)
        return ans
        