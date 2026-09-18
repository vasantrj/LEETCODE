"""
Problem: Decode String
LeetCode ID: 394
Pattern: Stack / String
Difficulty: Medium
Time Complexity: O(n + k)
Space Complexity: O(n + k)

Approach:
1. Traverse the encoded string from left to right.
2. Maintain:
   - current_num: the repetition count currently being built.
   - current_str: the string being constructed at the current nesting level.
   - stack: stores the string and repetition count from outer nesting levels.
3. When a digit is encountered, build the complete number. This handles
   multi-digit repetition counts such as 12[a].
4. When '[' is encountered:
   - Save the current string and repetition count on the stack.
   - Reset current_str and current_num to process the contents inside
     the brackets.
5. When ']' is encountered:
   - Pop the previous string and repetition count from the stack.
   - Repeat the current string the required number of times.
   - Append it to the string from the previous nesting level.
6. When a normal character is encountered, append it to current_str.
7. After processing the entire input, current_str contains the decoded
   string.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char
        
        return current_str