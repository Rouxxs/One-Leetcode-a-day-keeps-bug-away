class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n):
            base = ""
            num = n
            while num:
                r = int(num % i)
                base += str(r)
                num //= i
            if base==base[::-1]:
                continue
            else:
                return False
        return True