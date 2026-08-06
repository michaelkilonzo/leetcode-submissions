class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} # key: num, freq_map[num]: freq 
        freq_list = [[] for i in range(len(nums) + 1)] # i: freq, freq_list[i]: List[int]
        res = [] 

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        for num, freq in freq_map.items():
            freq_list[freq].append(num)
        
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res 


        