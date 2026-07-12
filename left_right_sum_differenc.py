# 2574. Left and Right Sum Differences
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        sum_array = []
        for i in range(len(nums)):
            sum_array.append(abs(sum(nums[:i+1])- sum(nums[i+1:])))
        return sum_array
    


if __name__ == "__main__":
    sol = Solution()
    mass = 5
    # landStartTime = [2,8]
    # landDuration = [4,1] 
    # waterStartTime = [6] 
    # waterDuration = [3]
    # ans = sol.earliestFinishTime(landStartTime,landDuration,waterStartTime,waterDuration)
    # print(ans)
    landStartTime = [5]
    landDuration = [3]
    waterStartTime = [1]
    waterDuration = [10]
    ans = sol.earliestFinishTime(landStartTime,landDuration,waterStartTime,waterDuration)
    print(ans)
#    abs