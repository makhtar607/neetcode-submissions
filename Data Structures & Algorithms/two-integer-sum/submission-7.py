class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for index, key in enumerate(nums):
            diff = target - key
            if diff in indexes:
                return [indexes[diff], index]
            indexes[key] = index
        
            