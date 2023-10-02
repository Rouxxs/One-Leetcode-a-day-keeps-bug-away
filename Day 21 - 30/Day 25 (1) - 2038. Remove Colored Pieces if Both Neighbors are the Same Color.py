class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        countA = 0
        countB = 0


        for i in range(0, len(colors)):
            if colors[i] == 'A':
                countA += 1
            else:
                if countA >= 3:
                    alice += countA - 2
                countA = 0
            if colors[i] == 'B':
                countB += 1
            else:
                if countB >= 3:
                    bob += countB - 2
                countB = 0
        
        if colors[-1] == 'A':
            if countA >= 3:
                alice += countA - 2
        else:
            if countB >= 3:
                bob += countB - 2
        return alice > bob