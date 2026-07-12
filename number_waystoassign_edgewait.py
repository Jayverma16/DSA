# 3558. Number of Ways to Assign Edge Weights I
from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges):
        MOD = 10**9 + 7
        n = len(edges) + 1

        graph = defaultdict(list)

        for u, v in edges:
            print(u,v)
            graph[u].append(v)
            graph[v].append(u)

        print(graph)
        q = deque([(1, 0)])  # (node, depth)
        visited = {1}
        print(q)
        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, depth + 1))

        return pow(2, max_depth - 1, MOD)
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.assignEdgeWeights([[1,2],[1,3],[3,4],[3,10]])#
    print(result)