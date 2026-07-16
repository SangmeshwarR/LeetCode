#  169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cand,count = 0,0

        for num in nums:
            if count == 0:
                cand = num

            if num == cand:
                count += 1
            else:
                count -= 1

        return cand