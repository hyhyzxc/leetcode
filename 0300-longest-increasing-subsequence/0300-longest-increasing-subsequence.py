class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]

        dp[0] = 1
        for i in range(1, len(nums)):
            curr = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr = max(curr, dp[j])
            dp[i] = curr + 1
        return max(dp)
