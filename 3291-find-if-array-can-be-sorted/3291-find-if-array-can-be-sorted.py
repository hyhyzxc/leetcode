class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # insertion sort
        sortedNums = sorted(nums)
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j] < nums[j-1]:
                if bin(nums[j-1]).count("1") == bin(nums[j]).count("1"):
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                else:
                    break
                j -= 1
             
        
        return nums == sortedNums