# My solution (Not an optimal solution, not constant extra space)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        tmp = [0] * n

        for i in nums:
            tmp[i - 1] += 1

        for i in range(len(tmp)):
            if tmp[i] >= 2:
                return i + 1
            
# Optimal solution (Linked list cycle + Floyd's Cycle detection)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
            
        slow1 = 0
        while True:
            slow1 = nums[slow1]
            slow = nums[slow]
            if slow1 == slow:
                return slow
