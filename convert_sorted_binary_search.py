# Definition for a binary tree node.
# 108. Convert Sorted Array to Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self, level=0, prefix="Root: "):
        """Prints the entire tree structure visually."""
        # Print the right subtree first (so it appears on top)
        if self.right:
            self.right.display(level + 1, "R---- ")
            
        # Print the current node with indentation based on its depth
        print("    " * level + prefix + str(self.val))
        
        # Print the left subtree (so it appears on the bottom)
        if self.left:
            self.left.display(level + 1, "L---- ")

    # Optional: If you still want print(root) to work directly, 
    # you can build a string representation using a helper
    def __str__(self):
        lines = []
        def build_str(node, level=0, prefix="Root: "):
            if node:
                build_str(node.right, level + 1, "R---- ")
                lines.append("    " * level + prefix + str(node.val))
                build_str(node.left, level + 1, "L---- ")
        build_str(self)
        return "\n".join(lines)
class Solution:
    def sortedArrayToBST(self, nums: list[int]) :
        # length_l = len(nums)
        # mid = length_l//2
        

        def build(left ,right):
            if left > right :
                return None 
            # elif left == right
            print(left)
            print(right)
            print("######################")
            mid = (left + right)//2
            mid_node = TreeNode(nums[mid])
            mid_node.left = build(left,mid-1)

            mid_node.right = build(mid+1,right)

            return mid_node
        return build(0 , len(nums) -1 )

if __name__ == "__main__":
    sol = Solution()
    ans = sol.sortedArrayToBST([-10,-3,0,5,9])
    ans.display()