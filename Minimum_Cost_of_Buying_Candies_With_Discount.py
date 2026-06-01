# 2144. Minimum Cost of Buying Candies With Discount
class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        
        ans_cost = 0
        if len(cost)==2:
            ans_cost += cost[0] +cost[1] 
            return ans_cost

        elif len(cost) == 1:
            ans_cost += cost[0]
            return ans_cost

        while len(cost)>=2:
            for _ in range(2):
                print(cost)
                max_1 = max(cost)
                index_v = cost.index(max_1)
                ans_cost += max_1
                cost.pop(index_v) 
            if len(cost)<1:
                continue   
            max_ans = max(cost)
            index_v = cost.index(max_ans)
            cost.pop(index_v)
        
        if len(cost)==1:
            max_ans = max(cost)
            index_v = cost.index(max_ans)
            ans_cost +=max_ans
            cost.pop(index_v)
        return ans_cost

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