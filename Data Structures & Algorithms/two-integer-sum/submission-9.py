class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i, num in enumerate(nums):

            compliment = target - nums[i]

            if compliment in map:
                return [map[compliment], i]
                
            if num not in map:
                map[num] = i
            
            
                

                