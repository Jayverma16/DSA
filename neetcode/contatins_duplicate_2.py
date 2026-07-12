
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False


if __name__ == "__main__":
    # for i in range(0,5,3):
    #     print(i)
    sol = Solution()
    result = sol.containsNearbyDuplicate([1,2,3,1,1],5)
    print(result)
    result = sol.containsNearbyDuplicate([2,1,2],1)
    print(result)
