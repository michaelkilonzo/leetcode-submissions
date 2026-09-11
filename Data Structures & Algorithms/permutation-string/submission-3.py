class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {} 
        for c in s1:
            s1_freq[c] = s1_freq.get(c, 0) + 1

        s2_freq = {} 
        l = 0 
        for r in range(len(s2)):
            s2_freq[s2[r]] = s2_freq.get(s2[r], 0) + 1
            while s2_freq[s2[r]] > s1_freq.get(s2[r], 0):
                s2_freq[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True

        return False
