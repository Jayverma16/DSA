from typing import List
def jump(nums: List[int]) -> int:
    n = len(nums)
    memo = {}

    def backtrack(i):
        if i >= n - 1:
            return 0

        if i in memo:
            return memo[i]

        min_jumps = float('inf')
        for j in range(1, nums[i] + 1):
            min_jumps = min(min_jumps, 1 + backtrack(i + j))

        memo[i] = min_jumps
        return min_jumps

    return backtrack(0)

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    value = jump(nums=nums)
    print(value)