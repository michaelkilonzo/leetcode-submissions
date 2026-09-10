class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0 
        freq = {} 
        max_freq = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            # shrink window if curr window needs more than k replacements 
            while r - l + 1 - max_freq > k:
                freq[s[l]] -= 1  
                l += 1
                
            res = max(res, r - l + 1)


        return res