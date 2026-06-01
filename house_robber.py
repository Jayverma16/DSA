# 198. House Robber
class Solution:
    def rob(self, nums: list[int]) -> int:
        # def rob_amount(nums,i):
        cost_1= 0
        cost_2 = 0
        if len(nums)==1:
            return nums[i]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        for i in range(0,len(nums),2):
            
            cost_1 += nums[i]

        for i in range(1,len(nums),2):
            cost_2 += nums[i]

        return max(cost_2, cost_1)

            
            








if __name__ == "__main__":
    sol = Solution()
    ans = sol.rob([2,7,9,3,1])
    print(ans)
    house = [2, 1, 1, 2]
    ans = sol.rob(house)
    print(ans)