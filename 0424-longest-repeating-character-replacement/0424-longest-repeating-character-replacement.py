class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        res = 0

        l = 0
        r = 0

        while r < len(s):
            char = s[r]
            counts[ord(char) - ord('A')] += 1
            numChanged = sum(counts) - max(counts)
            if numChanged <= k:
                res = max(r-l+1, res)
            else:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
        return res
            