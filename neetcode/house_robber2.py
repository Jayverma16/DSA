class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
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
        return max(solve(nums[:-1]), solve(nums[1:]))
