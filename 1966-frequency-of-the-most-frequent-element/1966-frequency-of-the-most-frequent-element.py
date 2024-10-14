class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = r = 0
        res = 0
        cost = 0
        while r < len(nums):
            target = nums[r]
            if cost > k:
                cost -= (target - nums[l])
                l += 1
            else:
                res = max(res, r-l+1)
                if r == len(nums) - 1:
                    break
                
                cost += (nums[r+1] - target) * (r-l+1)
                r += 1
     
                
                
        return res