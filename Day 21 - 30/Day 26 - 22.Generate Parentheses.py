class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        def backtracking(nOpen, nClose):
            if nOpen == nClose == n:
                ans.append("".join(stack))
                return
            if nOpen < n:
                stack.append('(')
                backtracking(nOpen + 1, nClose)
                stack.pop()
            if nOpen > nClose:
                stack.append(')')
                backtracking(nOpen, nClose + 1)
                stack.pop()
        backtracking(0, 0)
        return ans
                
        