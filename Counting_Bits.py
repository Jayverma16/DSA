class Solution:
    def countBits(self, n: int) -> list[int]:

        answer = []

        for i in range(n+1):
            answer.append(i.bit_count())

        return answer
    

if __name__ == "__main__":
    sol = Solution()
    ans = sol.countBits(5)
    print(ans)