class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # only 1 str 
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        first = strs[0]
        last = strs[-1]

        for i in range(len(first)):
            # if last is shorter, or the char at i are different ->     prefix ends at  i.
            if i == len(last) or first[i] != last[i]:
                return first[:i]

        return first