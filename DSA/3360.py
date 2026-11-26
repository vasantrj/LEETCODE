"""
Problem: Stone Removal Game
LeetCode ID: 3360
Pattern: Simulation
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)

Approach:
1. Alice starts by removing 10 stones; each subsequent turn removes
   exactly one fewer stone than the previous turn.
2. Simulate the game: on each turn, the current player must remove
   `take` stones if at least that many remain.
3. If the current player cannot remove `take` stones (or take hits 0),
   that player loses.
4. Track whose turn it is; when the loop ends, the player to move loses,
   so Alice wins only if it is Bob's turn at that point.
"""


class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        alice_turn = True
        while take > 0 and n >= take:
            n -= take
            take -= 1
            alice_turn = not alice_turn
        return not alice_turn
    