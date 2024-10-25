class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        NumSet = set()
        for num in nums:
            if num in NumSet:
                return True
            NumSet.add(num)
        return False