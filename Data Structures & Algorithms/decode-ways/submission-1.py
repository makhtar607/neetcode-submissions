class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        prev2, prev1 = 1, 1
        
        for i in range(1, len(s)):
            current = 0
            
            # Single-digit valid check
            if s[i] != '0':
                current += prev1
            
            # Two-digit valid check via character comparisons (avoids int slicing)
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                current += prev2
            
            # Early exit if current state becomes unreachable
            if current == 0:
                return 0
            
            prev2, prev1 = prev1, current
            
        return prev1