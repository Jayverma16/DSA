class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        one_s = self.climbStairs(n-1)
        sec_s = self.climbStairs(n-2)
        return one_s + sec_s
