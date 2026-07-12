class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # nums = sorted(nums)
        nums.sort()
        n = len(nums)
        print(nums)
        for i in range(n-1):
                
            if nums[i+1] == nums[i]:
                return True
        return False 
if __name__ == "__main__":
    sol = Solution()
    result = sol.hasDuplicate([1,2,3,1,2,3])
    print(result)