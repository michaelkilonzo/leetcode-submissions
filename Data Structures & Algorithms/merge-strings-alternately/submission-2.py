class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i, j = 0, 0

        # concat chars to res until end of at least one word
        while i < len(word1) and j < len(word2):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1
        
        # concat remaining chars to res 
        res += word1[i:]
        res += word2[j:]

        return res 

        