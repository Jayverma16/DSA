# 3633. Earliest Finish Time for Land and Water Rides I
class Solution:
    def earliestFinishTime(self, landStartTime: list[int],
                            landDuration: list[int],
                            waterStartTime: list[int],
                            waterDuration: list[int]) -> int:
        
        #what the fuck 
        
        # take land first
        min_s_land_time =  float('inf') 
        
        for i in range(len(landDuration)):
            land_finish = landDuration[i] + landStartTime[i]
            for j in range(len(waterDuration)):
                if waterStartTime[j] >= land_finish:
                    print(min(min_s_land_time,waterDuration[j]+ waterStartTime[j]))
                    min_s_land_time = min(min_s_land_time,waterDuration[j]+ waterStartTime[j])
        # take water first 
        min_s_water_time = float('inf') 
        for i in range(len(waterDuration)):
            water_finish = waterStartTime[i] + waterDuration[i]
            for j in range(len(landDuration)):
                if landStartTime[j] >= water_finish:
                    min_s_water_time = min(min_s_water_time,landDuration[j]+ landStartTime[j])
        return min(min_s_water_time,min_s_land_time)


    
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
   