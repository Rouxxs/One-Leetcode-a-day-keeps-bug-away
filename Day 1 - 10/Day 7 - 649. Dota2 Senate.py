class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        rad = deque([i for i in range(n) if (senate[i] == "R")])
        dire = deque([i for i in range(n) if (senate[i] == "D")])

        while rad and dire:
            r = rad.popleft()
            d = dire.popleft()
            if (r < d):
                rad.append(r + n)
            else:
                dire.append(d + n)
        
        return "Radiant" if rad else "Dire"