class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) 
        seq_map = {} 
        seq_len = 0 

        # get start of sequences 
        for num in nums_set: 
            if num - 1 not in nums_set:
                seq_map[num] = set() 
        
        # build sequences 
        for seq_start in seq_map: 
            n = seq_start
            while n + 1 in nums_set:
                n += 1 
                seq_map[seq_start].add(n)

        # find longest sequence 
        for k, v in seq_map.items():
            if len(v) + 1 > seq_len:
                seq_len = len(v) + 1 
        
        return seq_len