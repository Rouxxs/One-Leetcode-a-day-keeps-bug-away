class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            mid = l + (r - l) // 2

            time = 0
            for p in piles:
                time += math.ceil(float(p) / mid)
            if time <= h:
                ans = min(mid, ans)
                r = mid - 1
            else:
                l = mid + 1
        return ans
