
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        res = ""
        minLen = float("inf")
        l = 0

        t_freq = {}
        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        win_freq = {}
        formed = 0
        required = len(t_freq)

        for r in range(len(s)):
            c = s[r]

            if c in t_freq:
                win_freq[c] = win_freq.get(c, 0) + 1

                if win_freq[c] == t_freq[c]:
                    formed += 1

            while formed == required:
                if r - l + 1 < minLen:
                    res = s[l:r + 1]
                    minLen = r - l + 1

                left_char = s[l]

                if left_char in t_freq:
                    if win_freq[left_char] == t_freq[left_char]:
                        formed -= 1

                    win_freq[left_char] -= 1

                l += 1

        return res