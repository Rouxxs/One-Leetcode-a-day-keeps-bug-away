class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        sum = -10000

        for num in nums:
            # if temp < 0 and num > temp:
            #     temp = num
            # elif num <= 0:
            #     if temp - num > 0:
            #         temp += num
            #     else:
            #         temp = num
            # else:
            #     temp += num

            temp += num
            if temp < num:
                temp = num

            if temp > sum:
                sum = temp
        return sum