class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        store = [0] * (len(num1) + len(num2))
        print(int(num1[0]))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1,-1, -1):
                print(i)
                store[i+j+1] += int(num1[i]) * int(num2[j])
                store[i+j] += int(store[i+j+1] / 10)
                store[i+j+1] %= 10
        
        print(store)
        i = 0
        ans = ""
        while(store[i]==0): 
            if i + 1 >= len(store):
                break
            i += 1
        while(i < len(store)):
            ans += str(store[i])
            i += 1
        return ans