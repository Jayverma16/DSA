# 1331. Rank Transform of an Array
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        table = sorted(list(set(arr)))
        print(table)
        return [table.index(i)+1 for i in arr]
if __name__ == "__main__":

    sol = Solution()
    result = sol.arrayRankTransform([40,10,20,30])
    print(result)