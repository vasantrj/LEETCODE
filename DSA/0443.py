"""
Problem: String Compression
LeetCode ID: 443
Pattern: Two Pointers / String
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Use two pointers:
   - read scans through the original character array.
   - write tracks the position where compressed characters should be written.
2. For each group of consecutive identical characters:
   - Store the current character.
   - Count how many times it appears consecutively.
3. Write the character at the current write position and move write forward.
4. If the count is greater than 1, convert the count to a string and write
   each digit into the character array.
5. Continue until all characters have been processed.
6. Return write, which represents the length of the compressed array.
7. The compression is performed in-place, so no separate result array is
   required.
"""


class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0  
        read = 0  
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write

    