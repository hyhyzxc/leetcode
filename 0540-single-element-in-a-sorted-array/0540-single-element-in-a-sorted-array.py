class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 3:
            if nums[0] == nums[1]:
                return nums[2]
            else:
                return nums[0]

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            else:
                next = mid + 1
                if nums[mid] == nums[mid-1]:
                    mid -= 1
                    next = mid + 1
                if mid - l == 1:
                    return nums[mid-1]
                elif len(nums) - next - 1 == 1:
                    return nums[next+1]
                if (mid-l) % 2:
                    r = mid - 1
                else:
                    l = next + 1
        return nums[l]
      