class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            if target-num not in map:
                map[num] = i
            else:
                return [map[target-num], i]
                