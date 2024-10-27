class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            currStr = s[i:]
            length = len(currStr)
            for word in wordDict:
                string = currStr
                if length >= len(word):
                    string = string[0: len(word)]
             
                if string == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
        return dp[0]
            