
"""
Problem: Daily Temperatures
LeetCode ID: 739
Pattern: Monotonic Stack
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Initialize an answer array with zeros because some days may
   have no warmer future temperature.
2. Maintain a stack of indices whose temperatures have not yet
   encountered a warmer day. The stack is monotonic decreasing
   by temperature.
3. Iterate through temperatures with their indices.
4. While the current temperature is warmer than the temperature
   at the top index of the stack, pop that index.
5. Calculate the waiting time for the popped index as the current
   index minus the popped index.
6. Push the current index onto the stack.
7. Return the answer array.
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer
