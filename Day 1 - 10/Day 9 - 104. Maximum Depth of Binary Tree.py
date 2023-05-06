# I feel kinda lazy today, so I chose a pretty ez question
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def ans(head):
            if not (head): return 0
            return 1 + max(ans(head.left), ans(head.right))
        return ans(root)