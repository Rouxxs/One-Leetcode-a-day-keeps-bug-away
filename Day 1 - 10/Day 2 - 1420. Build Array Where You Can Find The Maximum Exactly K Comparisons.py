import numpy as np
class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        # dp = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
        dp = np.zeros((n+1, k+1, m+1), dtype=int).tolist()

        #print(dp)
        for i in range(1, m+1):
            dp[1][1][i] = 1

        for i, j, k_ in itertools.product(range(1, n+1), range(1, k+1), range(1, m+1)):
            dp[i][j][k_] += dp[i-1][j][k_] * k_
            dp[i][j][k_] += sum(dp[i-1][j-1][1:k_])
        print(dp)
        return sum(dp[n][k][1:]) % (10 ** 9 + 7)