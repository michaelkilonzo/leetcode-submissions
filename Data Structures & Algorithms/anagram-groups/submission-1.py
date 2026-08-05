class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        alphabet_dict = {chr(ord('a') + i): i for i in range(26)}   
        for s in strs:
            letter_count = [0 for i in range(26)]
            for c in s: 
                letter_count[alphabet_dict[c]] += 1
            if tuple(letter_count) in res_dict:
                res_dict[tuple(letter_count)].append(s)
            else:
                res_dict[tuple(letter_count)] = [s]

        return list(res_dict.values())