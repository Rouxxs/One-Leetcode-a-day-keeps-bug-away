class Solution:
    def minCapability(self, A: List[int], k: int) -> int:
        B = list(A)
        B.sort()
        print(B)
        print(A)
        l, r = 0, len(B) - 1
        while l < r:
            m = (l + r) // 2
            last = take = 0
            for a in A:
                if last:
                    last = 0
                    continue
                if a <= B[m]:
                    take += 1
                    last = 1
            if take >= k:
                r = m
            else:
                l = m + 1
        return B[l]