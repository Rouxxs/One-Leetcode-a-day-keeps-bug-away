class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        ans = 0

        for n in nums:
            if n - 1 not in setNums:
                length = 1
                while n + length in setNums:
                    length += 1
                ans = max(ans, length)

        return ans