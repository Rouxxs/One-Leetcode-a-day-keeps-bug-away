# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def recursion(root):
            nonlocal ans
            if not root:
                return 0
            l = recursion(root.left)
            r = recursion(root.right)
            ans = max(ans, l + r)
            return max(l, r) + 1
        recursion(root)
        return ans