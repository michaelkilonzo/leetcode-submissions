class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1

        l = 0
        substr_freq = {} 
        for r in range(len(s2)):
            substr_freq[s2[r]] = substr_freq.get(s2[r], 0) + 1
            while substr_freq[s2[r]] > s1_freq.get(s2[r], 0):
                substr_freq[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True
    
        return False

