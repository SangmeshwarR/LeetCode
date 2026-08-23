# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = set(nums)
        res = []

        for n in range(1, len(nums) + 1):
            if n not in numbers:
                res.append(n)
        
        return res