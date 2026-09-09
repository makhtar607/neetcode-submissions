class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for num in nums:
            if num not in map:
                map.add(num)
        return len(map) < len(nums)

            