# 3614. Process String with Special Operations II
class Solution:
    def processStr(self, s: str, k: int) -> str:
        result = []
        for char_ in s:
            if char_ == "#":
                result = result + result
                continue

            if char_ == "*":
                if result != []:
                    result.pop()
                continue
            if char_ == "%":

                result.reverse()
                continue
            
            result.append(char_)
        if len(result) <= k or len(result)==0:
            return "."
            
        return result[k]
if __name__ == "__main__":
    sol = Solution()
    result = sol.processStr(["a#b%*"],1)
    print(result)