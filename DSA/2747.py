"""
Problem: Count Zero Request Servers
LeetCode ID: 2747
Pattern: Sorting / Sliding Window / Two Pointers
Difficulty: Medium
Time Complexity: O(m log m + q log q)
Space Complexity: O(n + q)

Approach:
1. Sort the server logs by their timestamps.
2. Sort query indices based on their query times while
   preserving the original positions for the final answers.
3. Maintain a sliding window of logs whose timestamps fall
   within the interval [query - x, query].
4. Use cnt to track the number of active logs for each server.
5. Use active to count how many servers have at least one
   log inside the current time window.
6. Add logs with timestamps less than or equal to the query time.
7. Remove logs with timestamps strictly less than query - x.
8. Calculate the number of inactive servers as n - active.
9. Store each answer at its original query index and return
   the result array.
"""

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda l: l[1])
        order = sorted(range(len(queries)),key=lambda i: queries[i])
        cnt = [0] * (n + 1)
        active = 0
        l = r = 0
        res = [0] * len(queries)
        for i in order:
            q = queries[i]
            while r < len(logs) and logs[r][1] <= q:
                s = logs[r][0]
                if cnt[s] == 0:
                    active += 1
                cnt[s] += 1
                r += 1

            while l < r and logs[l][1] < q - x:
                s = logs[l][0]
                cnt[s] -= 1
                if cnt[s] == 0:
                    active -= 1

                l += 1
            res[i] = n - active
        return res