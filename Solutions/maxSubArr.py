# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        sum = 0

        for i in nums:
            if sum < 0:
                sum = 0
            sum += i
            maxSub = max(maxSub,sum)
        return maxSub
                