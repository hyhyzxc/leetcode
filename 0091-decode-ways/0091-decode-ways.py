class Solution:
    def numDecodings(self, s: str) -> int:
        # jump once or jump twice
        dp = [0] * len(s)
        
        if s[0] == "0":
            dp[0] = 0
        else:
            dp[0] = 1
        
        if len(s) == 1:
            return dp[0]
        if s[1] == "0":
            if int(s[0:2]) <= 26 and int(s[0:2]) >= 10:
                dp[1] = 1
            else:
                dp[1] = 0
        else:
            if dp[0] == 0:
                dp[1] = 0
            else:
                if int(s[0:2]) <= 26:
                    dp[1] = 2
                else:
                    dp[1] = 1
        
        for i in range(2, len(s)):
            if s[i] == "0":
                if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 0
            else:
                if s[i-1] == "0":
                    dp[i] = dp[i-1]
                else:
                    if int(s[i-1:i+1]) > 26:
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[-1]

        
            

            
       
            

            