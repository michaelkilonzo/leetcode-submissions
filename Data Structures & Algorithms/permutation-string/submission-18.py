class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for c in s1:
            s1_freq[c] = s1_freq.get(c, 0) + 1

        
        subStr_freq = {} 
        l = 0 
        for r in range(len(s2)):
            subStr_freq[s2[r]] = subStr_freq.get(s2[r], 0) + 1
            while r - l + 1 > len(s1):
                subStr_freq[s2[l]] -= 1
                if subStr_freq[s2[l]] == 0:
                    del subStr_freq[s2[l]]
                l += 1
            if subStr_freq == s1_freq:
                return True
            
        return False