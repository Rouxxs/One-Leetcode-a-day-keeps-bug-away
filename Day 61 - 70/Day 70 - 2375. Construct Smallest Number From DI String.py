class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        ans = []

        for i in range(len(pattern) + 1):
            # add the hightest number you will need to stack
            stack.append(i + 1)

            print(stack)

            # consume from stack
            if i == len(pattern) or pattern[i] == 'I':
                print(i)
                while stack:
                    ans.append(str(stack.pop()))

        return ''.join(ans)