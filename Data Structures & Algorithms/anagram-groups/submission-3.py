class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        alphabet_dict = {chr(ord('a') + i): i for i in range(26)}   
        for s in strs:
            letter_count = [0 for i in range(26)]
            for c in s: 
                letter_count[alphabet_dict[c]] += 1
            letter_count = tuple(letter_count)
            if letter_count in res_dict:
                res_dict[letter_count].append(s)
            else:
                res_dict[letter_count] = [s]

        return list(res_dict.values())