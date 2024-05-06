class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        ans = [0] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mx:
                ans[i] = 1
        return ans