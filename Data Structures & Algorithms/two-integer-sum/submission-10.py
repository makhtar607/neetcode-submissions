class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i, num in enumerate(nums):

            compliment = target - nums[i]
            if compliment in map:
                return [map[compliment], i]
            map[num] = i
            
            
                

                