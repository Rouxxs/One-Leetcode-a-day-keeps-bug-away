# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            leftMax = max(leftMax, 0)
            rightMax = dfs(root.right)
            rightMax = max(rightMax, 0)

            ans = max(ans, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return ans