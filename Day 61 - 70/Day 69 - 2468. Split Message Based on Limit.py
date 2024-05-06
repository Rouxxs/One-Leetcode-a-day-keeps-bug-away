class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        # Find k so that we can split the message into k parts
        total = 0 #len(str(1)) + len(str(2)) + ... + len(str(k))
        k = 0
            # check if there is enough chars  
            # to split the last part
        while 3 + len(str(k)) * 2 < limit and total + len(message) + (3 + len(str(k))) * k > limit * k :
            k += 1
            total += len(str(k))
        
        ans = []
        if 3 + len(str(k)) * 2 < limit:
            i = 0
            for j in range(1, k + 1):
                l = limit - (3 + len(str(j)) + len(str(k)))
                ans.append(message[i:i + l] + "<" + str(j) + '/' + str(k) + '>')
                i += l
        return ans