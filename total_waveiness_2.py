# 3753. Total Waviness of Numbers in Range II

from functools import cache

def solve(num):
    if num < 100:
        return 0

    s = str(num)
    n = len(s)

    @cache
    def dfs(pos, prev, curr, tight, leading):
        # Reached end of number
        if pos == n:
            return (1, 0)   # (count, total_waviness)

        up = int(s[pos]) if tight else 9

        total_cnt = 0
        total_sum = 0

        for digit in range(up + 1):

            new_tight = tight and (digit == up)
            new_leading = leading and (digit == 0)

            if new_leading:
                new_prev = -1
                new_curr = -1
            else:
                if leading:
                    # first non-zero digit
                    new_prev = -1
                    new_curr = digit
                else:
                    new_prev = curr
                    new_curr = digit

            sub_cnt, sub_sum = dfs(
                pos + 1,
                new_prev,
                new_curr,
                new_tight,
                new_leading
            )

            total_cnt += sub_cnt
            total_sum += sub_sum

            # Check if curr forms peak/valley
            if not leading and prev != -1:
                if (prev < curr > digit) or (prev > curr < digit):
                    total_sum += sub_cnt

        return (total_cnt, total_sum)

    return dfs(0, -1, -1, True, True)[1]


def total_waviness_in_range(l, r):
    return solve(r) - solve(l - 1)
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        return total_waviness_in_range(num1,num2)
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
   