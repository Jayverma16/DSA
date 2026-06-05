# 3751. Total Waviness of Numbers in Range I

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_wave = 0
        dp = {i:0 for i in range(100) }
        
        for num in range(num1,num2+1):
            if num in dp:
                total_wave + dp[num]
                continue
            digit_array = [int(digit) for digit in str(num)]
            # find wave or vally 
            wave = 0
            for digit_ind in range(len(digit_array)-2):
                if digit_array[digit_ind] < digit_array[digit_ind+1] > digit_array[digit_ind+2] :
                    wave +=1
                elif digit_array[digit_ind] > digit_array[digit_ind+1] < digit_array[digit_ind+2]:
                    wave +=1
            dp[num] = wave
            total_wave+= wave
        return total_wave





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
   