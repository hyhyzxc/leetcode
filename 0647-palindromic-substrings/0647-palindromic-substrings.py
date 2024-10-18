class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l -= 1
                r += 1
            
            l = i
            r = i+1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l -= 1 
                r += 1
        return res
            