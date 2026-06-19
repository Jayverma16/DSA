# 1061. Lexicographically Smallest Equivalent String
class UnionFind:
    def __init__(self):
        self.ids = list(range(26))

    def find(self, ch):
        idx = ord(ch) - ord('a')
        

        while idx != self.ids[idx]:
            self.ids[idx] = self.ids[self.ids[idx]]  # path compression
            idx = self.ids[idx]

        return idx

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)

        if x < y:
            self.ids[y] = x
        else:
            self.ids[x] = y
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uno = UnionFind()
        n = len(s1)
        for i in range(n):
            uno.union(s1[i],s2[i])
        
        small_lexi = ''
        for ch in baseStr:
            small_lexi += chr(uno.find(ch) +ord("a"))
        return small_lexi
        
if __name__ == "__main__":
    # uf = UnionFind()

    # uf.union('a', 'c')
    # uf.union('c', 'e')

    # print(chr(uf.find('e') + ord('a')))  # 
    sol = Solution()
    result = sol.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser")
    print(result)