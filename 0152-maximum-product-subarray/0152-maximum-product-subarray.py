class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = n * curMax
            curMax = max(n * curMax, max(n, n* curMin))
            curMin = min(temp, min(n, n*curMin))
            res = max(res, curMax)
        return res