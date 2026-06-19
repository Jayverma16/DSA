# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        hig_alt = 0
        n = len(gain)
        pre_alt = 0

        for i in range(n):
            hig_alt = max(hig_alt,  gain[i] + pre_alt )
            pre_alt =  gain[i] + pre_alt 
        return hig_alt
    

if __name__ =="__main__":
    sol = Solution()
    result = sol.largestAltitude([-5,1,5,0,-7]) # answe is 1
    print(result)