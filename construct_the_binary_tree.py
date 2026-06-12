# # Definition for a binary tree node.
# 2196. Create Binary Tree From Descriptions
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) :
        node = {}
        children = set()
        for parent, child, isLeft in descriptions:

            if parent not in node:
                node[parent] = TreeNode(parent)
            if child not in node:
                node[child] = TreeNode(child)

            if isLeft:
                node[parent].left = node[child]
            else:
                node[parent].right = node[child]
            
            children.add(child)

        for parent, _, _ in descriptions:
            if parent not in children:
                return node[parent]

if __name__ == "__main__":
    sol = Solution()
    ans = sol.createBinaryTree([-10,-3,0,5,9])
    # print(ans)