"""
Problem: Image Overlap
LeetCode ID: 835
Pattern: Arrays / Hashing / Coordinate Shifting
Difficulty: Medium
Time Complexity: O(n^4)
Space Complexity: O(n^2)

Approach:
1. Store the coordinates of all cells containing 1 in img1 and img2.
2. If either image contains no 1s, return 0 because there can be no
   overlapping cells.
3. For every pair of 1-cells, one from each image:
   - Calculate the translation required to move the cell from img2
     onto the cell from img1.
   - Store this translation as a coordinate shift.
4. Count how many pairs produce each shift using a hash map.
5. A shift with the highest frequency represents the maximum number
   of 1-cells that overlap after applying that translation.
6. Return the maximum shift frequency.
"""

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        if not ones1 or not ones2:
            return 0
        
        shift_counts = defaultdict(int)
        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r1 - r2, c1 - c2)
                shift_counts[shift] += 1
        
        return max(shift_counts.values())