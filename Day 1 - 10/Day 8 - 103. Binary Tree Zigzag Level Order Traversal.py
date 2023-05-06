# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        def recursion(i, head):
            if len(ans) <= i:
                ans.append([head.val])
            else: 
                ans[i].append(head.val)
            i += 1
            if head.left:
                recursion(i, head.left)
            if head.right:
                recursion(i, head.right)
        if root:
            recursion(0, root)
        for i in range(1, len(ans), 2):
            ans[i].reverse()
        return ans
                