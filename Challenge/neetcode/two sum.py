class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        NumsMap = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in NumsMap:
                return [NumsMap[complement], i]
            NumsMap[num] = i