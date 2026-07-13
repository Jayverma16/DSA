class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            n = len(arr)
            dp = [-1] * n

            def maxrob(i):
                if i >= n:
                    return 0
                if dp[i] != -1:
                    return dp[i]

                first = maxrob(i + 1)
                second = arr[i] + maxrob(i + 2)

                dp[i] = max(first, second)
                return dp[i]

            return maxrob(0)