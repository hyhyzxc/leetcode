class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        combined = list(zip(scores, ages))
        combined.sort(key = lambda x: (x[1], x[0]))
      
        dp = [0] * len(combined)
        ans = 0
        for i in range(len(dp)):
            score, age = combined[i]
            dp[i] = score
            for j in range(i):
                if combined[j][0] <= score and dp[j] + score > dp[i]:
                    dp[i] = dp[j] + score
            
            ans = max(ans, dp[i])
        return ans



