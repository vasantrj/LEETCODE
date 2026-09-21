"""
Problem: Asteroid Collision
LeetCode ID: 735
Pattern: Stack / Simulation
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use a stack to store asteroids that are still alive after all
   possible collisions with previously processed asteroids.
2. Traverse each asteroid from left to right.
3. A collision can occur only when:
   - The current asteroid is moving left (`a < 0`).
   - The top asteroid in the stack is moving right (`stack[-1] > 0`).
4. Compare the sizes of the two colliding asteroids:
   - If the stack asteroid is smaller, remove it and continue checking
     the current asteroid against the next asteroid in the stack.
   - If both have the same size, remove the stack asteroid and mark
     the current asteroid as destroyed.
   - If the stack asteroid is larger, the current asteroid is destroyed.
5. If the current asteroid survives all collisions, add it to the stack.
6. The remaining stack contains the asteroids that survive all
   collisions.
"""

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                top = stack[-1]
                if top < -a:
                    stack.pop()
                elif top == -a:
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(a)
        return stack
    