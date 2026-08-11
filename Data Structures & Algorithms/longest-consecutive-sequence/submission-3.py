class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) 
        longest_seq_len = 0 

        for num in nums_set: 
            # find start of sequences 
            if num - 1 not in nums_set:
                # count sequence length 
                curr_seq_len = 1 
                while num + 1 in nums_set:
                    curr_seq_len += 1
                    num += 1
                longest_seq_len = max(longest_seq_len, curr_seq_len)

        return longest_seq_len
        