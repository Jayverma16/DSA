class Solution:
    def __init__(self):
        self.db = {0: 1, 1: 1}

    def climbStairs(self, n: int) -> int:
        if n in self.db:
            return self.db[n]

        self.db[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.db[n]
