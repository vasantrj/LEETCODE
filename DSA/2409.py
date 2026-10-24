
"""
Problem: Count Days Spent Together
LeetCode ID: 2409
Pattern: Arrays / Date Conversion / Interval Overlap
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Store the number of days in each month of a non-leap year.
2. Build a prefix-sum array to calculate the day number for
   any date in the year.
3. Define to_day() to convert an MM-DD date into its day number.
4. Find the later of Alice's and Bob's arrival dates as the
   beginning of their potential overlap.
5. Find the earlier of their departure dates as the end of
   their potential overlap.
6. Return the inclusive overlap length, or zero if the intervals
   do not overlap.
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0]
        for d in days:
            prefix.append(prefix[-1] + d)

        def to_day(s: str) -> int:
            m, d = int(s[:2]), int(s[3:])
            return prefix[m - 1] + d

        start = max(to_day(arriveAlice), to_day(arriveBob))
        end = min(to_day(leaveAlice), to_day(leaveBob))
        return max(0, end - start + 1)
        