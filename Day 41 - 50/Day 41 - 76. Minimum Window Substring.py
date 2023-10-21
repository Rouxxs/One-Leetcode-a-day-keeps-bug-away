class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t
        countT, windowCount = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        l = 0
        have, need = 0, len(countT)
        res, minLength = [-1, -1], float('inf')

        for r in range(len(s)):
            c = s[r]
            windowCount[c] = 1 + windowCount.get(c, 0)

            if c in countT and windowCount[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    res = [l, r]
                windowCount[s[l]] -= 1
                if s[l] in countT and windowCount[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]: res[1] + 1] if minLength != float('inf') else ""