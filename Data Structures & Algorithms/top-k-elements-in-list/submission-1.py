class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        frequency_bucket = [[] for i in range(len(nums)+ 1)]
        #creates frequency map
        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] +=1
        

       #adds key to the index which is frequency occurs
        for key, val in frequency_map.items():
            frequency_bucket[val].append(key)

            
        res = []
        #loops backwords through bucket sorted array
        for i in range(len(frequency_bucket)-1, 0, -1):
            #adds each value in each frequency bucket with backwards scan because right side larger K
        
            for n in frequency_bucket[i]:
                res.append(n)
                #if the length of the result is equal to top k value then it is done
                if len(res) == k:
                    return res



        
            
            