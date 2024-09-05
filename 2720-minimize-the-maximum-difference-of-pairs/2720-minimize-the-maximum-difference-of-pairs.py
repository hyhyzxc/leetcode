class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(threshold):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= threshold:
                    count += 1
                    if count == p:
                        return True
                    i += 2
                else:
                    i += 1
            return False

        nums.sort()
        if p == 0:
            return 0
        l = 0 
        r = nums[-1]
        res = 10**9

        while l <= r:
            mid = l + (r-l) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res