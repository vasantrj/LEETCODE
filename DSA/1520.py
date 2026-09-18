"""
Problem: Maximum Number of Non-Overlapping Substrings
LeetCode ID: 1520
Pattern: Greedy / Intervals / String
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Record the first and last occurrence of every character in the string.
2. For each character, start with its first occurrence as the beginning
   of a candidate substring and its last occurrence as the end.
3. Expand the candidate interval whenever a character inside the interval
   has a last occurrence beyond the current end.
4. If a character inside the interval has its first occurrence before the
   candidate's starting position, the interval is invalid because it would
   exclude an earlier occurrence of that character.
5. Store every valid interval.
6. Sort the valid intervals by their ending positions.
7. Use a greedy interval-selection strategy:
   - Select the first interval that starts after the end of the previously
     selected interval.
   - Since intervals are processed by increasing end position, this leaves
     as much remaining space as possible for future substrings.
8. Return the selected substrings.
"""


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        intervals = []
        for c, start in first.items():
            end = last[c]
            j = start
            valid = True
            while j <= end:
                c2 = s[j]
                if first[c2] < start:
                    valid = False
                    break
                end = max(end, last[c2])
                j += 1
            if valid:
                intervals.append((start, end))
        
        intervals.sort(key=lambda x: x[1])
        
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
        
        return res