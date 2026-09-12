"""
Problem: Maximum Score of Non-overlapping Intervals
LeetCode ID: 3414
Pattern: Dynamic Programming / Weighted Interval Scheduling / Binary Search
Difficulty: Medium
Time Complexity: O(n log n)
Space Complexity: O(n)

Approach:
1. Sort the intervals by their ending position while keeping their
   original indices.
2. For every interval, use binary search to find the first previous
   interval that does not overlap with it.
3. Use dynamic programming where dp[i][k] stores the maximum total
   weight that can be obtained from the first i intervals using exactly
   k intervals.
4. For each interval, consider two choices:
   - Skip the current interval and keep the previous DP result.
   - Take the current interval and combine its weight with the best
     compatible solution using k - 1 intervals.
5. Store the original indices of selected intervals along with their
   total weight so that ties can be resolved using lexicographically
   smaller indices.
6. Since at most four intervals can be selected, maintain DP states
   for k = 0 through 4.
7. After processing all intervals, compare all possible selections
   containing up to four intervals and return the one with the maximum
   total weight. If multiple selections have the same weight, return
   the lexicographically smallest list of indices.
"""


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])
        Ls = [intervals[i][0] for i in order]
        Rs = [intervals[i][1] for i in order]
        Ws = [intervals[i][2] for i in order]
        Idx = order
        NEG = float('-inf')
        dp = [None] * (n + 1)
        dp[0] = [(0, [])] + [(NEG, None)] * 4
        for i in range(1, n + 1):
            l = Ls[i - 1]
            w = Ws[i - 1]
            orig_idx = Idx[i - 1]
            p = bisect_left(Rs, l)
            prev = dp[i - 1]
            base_p = dp[p]
            cur_dp = [None] * 5
            cur_dp[0] = (0, [])
            for k in range(1, 5):
                opt1 = prev[k]
                if base_p[k - 1][0] == NEG:
                    opt2 = (NEG, None)
                else:
                    new_sum = base_p[k - 1][0] + w
                    new_list = sorted(base_p[k - 1][1] + [orig_idx])
                    opt2 = (new_sum, new_list)
                if opt2[0] > opt1[0]:
                    cur_dp[k] = opt2
                elif opt2[0] < opt1[0]:
                    cur_dp[k] = opt1
                else:
                    if opt1[0] == NEG:
                        cur_dp[k] = opt1
                    else:
                        cur_dp[k] = opt2 if opt2[1] < opt1[1] else opt1
            dp[i] = cur_dp
        best = dp[n][0]
        for k in range(1, 5):
            cand = dp[n][k]
            if cand[0] == NEG:
                continue
            if cand[0] > best[0] or (cand[0] == best[0] and cand[1] < best[1]):
                best = cand
        return best[1]

