class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        NumMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in NumMap:
                return [i, NumMap[complement]]
            NumMap[num]=i