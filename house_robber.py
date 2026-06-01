# 198. House Robber
class Solution:
    def rob(self, nums: list[int]) -> int:
        dp= [-1]*len(nums)
        def rob_money(nums, i):

            if i < 0:
                return 0
            rob_current = 0
            if dp[i] != -1:
                rob_current = dp[i]
            else:
                rob_current = nums[i]+ rob_money(nums,i-2)
                dp[i] = rob_current

            skip_current = rob_money(nums, i-1)

            return max(rob_current, skip_current)

        return rob_money(nums,len(nums) -1)






if __name__ == "__main__":
    sol = Solution()
    ans = sol.rob([2,7,9,3,1])
    print(ans)
    house = [2, 1, 1, 2]
    ans = sol.rob(house)
    print(ans)