class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        dp = [0 for i in range(len(s))]

        for i in range(len(s)):
            char = s[i]
            if i == 0:
                dp[0] = 1
                res += char
            else:
                if char == s[i-1]:
                    if dp[i-1] >= 2:
                        dp[i] = dp[i-1] + 1
                        continue
                    else:
                        dp[i] = dp[i-1] + 1
                        res += char
                else:
                    dp[i] = 1
                    res += char
        
        return res

                