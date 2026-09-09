class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            # 1. Build the frequency dictionary manually
            freq = {}
            for char in word:
                freq[char] = freq.get(char, 0) + 1
                
            # 2. Convert the dict items into a sorted, hashable tuple
            key = tuple(sorted(freq.items()))
            
            # 3. Group the word into the map
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(word)
            
        return list(anagram_map.values())