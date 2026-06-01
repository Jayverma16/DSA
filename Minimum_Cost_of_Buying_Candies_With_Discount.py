# 2144. Minimum Cost of Buying Candies With Discount
class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        total_cost = 0
        length_cost = len(cost)
        take = 0
        for i in range(length_cost):
            if take == 2:
                take = 0
                continue
            total_cost += cost[i] 
            take+=1
        return total_cost
    

if __name__ == "__main__":
    sol = Solution()
    ans = sol.minimumCost([1,2,3])
    print(ans)
    ans = sol.minimumCost([6,5,7,9,2,2])
    print(ans)
    ans = sol.minimumCost([5,5])
    print(ans)
    ans = sol.minimumCost([3,3,3,1])
    print(ans)
    cost = [2,10,5,4,3,10,5,10]
    ans = sol.minimumCost(cost)
    print(ans)