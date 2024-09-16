class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        nums = []
        for time in timePoints:
            nums.append(int(time[:2]) * 60 + int(time[3:]))
            if int(time[:2]) < 12:
                nums.append(nums[-1] + 24 * 60)
        nums.sort()
      
        res = 10 ** 5
        for i in range(1, len(nums)):
            res = min(res, min(nums[i] - nums[i-1], nums[i-1] + 24 * 60 - nums[i]))
        return res