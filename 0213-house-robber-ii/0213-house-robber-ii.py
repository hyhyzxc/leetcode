class Solution:
    def rob(self, nums: List[int]) -> int:

        def robber(start, end):
            #print(start, end)
            if start >= len(nums):
                return 0
            dp = [0] * (end-start+1)
            dp[0] = nums[start]
            if end-start + 1 > 1:
                dp[1] = max(nums[start+1], dp[0])
            
           
            for i in range(start+2, end+1):
                
                dp[i-start] = (max(dp[i-start-1], dp[i-start-2] + nums[i]))
            print(dp)
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        return max(robber(0, len(nums)-2), robber(1, len(nums)-1))


