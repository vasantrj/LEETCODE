"""
Problem: Dota2 Senate
LeetCode ID: 649
Pattern: Queue / Greedy Simulation
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
1. Use two queues to store the indices of Radiant and Dire senators.
2. Traverse the senate string and place each senator's index into
   the corresponding queue.
3. While both parties still have senators:
   - Remove the earliest available Radiant index and Dire index.
   - The senator with the smaller index gets to act first and bans
     the opposing senator.
4. If the Radiant senator acts first, add its index plus n back to the
   Radiant queue. This represents the same senator participating in
   the next round.
5. If the Dire senator acts first, add its index plus n back to the
   Dire queue for the next round.
6. Continue until one party's queue becomes empty.
7. The remaining party is the winning party.
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, c in enumerate(senate):
            if c == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"

    