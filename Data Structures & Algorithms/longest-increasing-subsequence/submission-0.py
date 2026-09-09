class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return length
        lengths = [1] * len(nums)
        for i in range(len(nums)):

            for j in range(i):

                if nums[j] < nums[i]:

                    lengths[i] = max(lengths[i], lengths[j] + 1)
        
        return max(lengths)
        
                
                
            

            

