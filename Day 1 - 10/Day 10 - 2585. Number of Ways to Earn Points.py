class Solution(object):
    def waysToReachTarget(self, target, types):
        """
        :type target: int
        :type types: List[List[int]]
        :rtype: int
        """
        dp = [1] + [0] * target
        for a, b in types:
            for i in range(target, -1, -1):
                for c in range(1, min(a, i // b) + 1):
                    dp[i] = (dp[i] + dp[i - b * c]) % (10 ** 9 + 7)
        return dp[target]