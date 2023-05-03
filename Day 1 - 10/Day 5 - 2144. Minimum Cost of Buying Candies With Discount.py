class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        print(cost)
        ans = 0
        for i in range(0, len(cost), 3):
            if i + 1 == len(cost):
                ans += cost[i]
            else:
                ans += cost[i] + cost[i+1]

        return ans