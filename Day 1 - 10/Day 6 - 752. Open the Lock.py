class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadSet = set(deadends)
        if "0000" in deadSet: 
            return -1
        
        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for i in range(4): 
                    digit = int(curr[i])
                    for shift in [-1, 1]:
                        new_digit = (digit + shift) % 10
                        new_code = curr[:i] + str(new_digit) + curr[i+1:]
                        if new_code in deadSet: continue
                        deadSet.add(new_code)
                        q.append(new_code)
            steps += 1
            
        return -1