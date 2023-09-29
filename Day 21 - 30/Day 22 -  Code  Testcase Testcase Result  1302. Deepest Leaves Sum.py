# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = {}
        dq = deque()
        dq.append((root, 0))
        while dq:
            node, l = dq.popleft()
            if l in d:
                d[l] += node.val
            else:
                d|={l:node.val}
            if node.left:
                dq.append((node.left, l+1))
            if node.right:
                dq.append((node.right, l+1))
        return list(d.values())[-1]

