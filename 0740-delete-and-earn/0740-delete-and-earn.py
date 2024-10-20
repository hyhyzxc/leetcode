from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        for num in nums:
            num_map[num] += 1
        
        nums = list(set(sorted(nums)))

        dp = [0] * len(nums)

        dp[0] = nums[0] * num_map[nums[0]]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                w = nums[i] * num_map[nums[i]]
                if i >= 2:
                    w += dp[i-2]
                dp[i] = max(dp[i-1], w)
            else:
                dp[i] = nums[i] * num_map[nums[i]] + dp[i-1]
        #print(dp)
        return dp[-1]