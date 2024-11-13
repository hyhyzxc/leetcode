class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        def binary_search_ceil(l, r, ceil):
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] <= ceil:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        def binary_search_floor(l, r, floor):
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] >= floor:
                    r = mid - 1
                else:
                    l = mid + 1
            return r

        for i in range(len(nums)-1):
            first = nums[i]
            second_ceil = upper - first
            second_floor = lower - first

            l = i+1
            r = len(nums) - 1
            floor = binary_search_floor(l, r, second_floor)
            ceil = binary_search_ceil(l, r, second_ceil)
            res += ceil - 1 - floor 
        return res