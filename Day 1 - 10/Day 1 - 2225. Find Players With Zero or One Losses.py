class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        win = []
        los = []

        for m in matches:
            win.append(m[0])
            los.append(m[1])

        first = []
        second = [] 
        count = Counter(los)
        for i in range(len(win)):
            if (count[win[i]] == 0):
                first.append(win[i])
            if (count[win[i]] == 1):
                second.append(win[i])
            if (count[los[i]] == 1):
                second.append(los[i])
        
 
        first = list(set(first))
        second = list(set(second))
        first.sort()
        second.sort()
        return [first, second]