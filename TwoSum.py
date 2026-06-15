#1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # pyright: ignore[reportUndefinedVariable]
        prevMap = {} #hashmap to contain all previous elements than the one being iterated currently
        for i,n in enumerate(nums): #stores key,value pairs while iterating
            diff = target - n 
            if diff in prevMap: #diff being in hashmap already means answer's found i.e. [2,7,11,5] and target 9: while on 7, diff = 9-7 = 2 hence ans. is arr[0] and arr[1]
                return[prevMap[diff],i] 
            prevMap[n] = i
            