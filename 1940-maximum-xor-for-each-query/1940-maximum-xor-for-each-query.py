class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        res = []
        currTotal = nums[0]
        for n in nums[1:]:
            currTotal = currTotal ^ n
        
        target = 2**maximumBit - 1
        res.append(target ^ currTotal)

        for i in range(len(nums) - 1, 0, -1):
            currTotal = currTotal ^ nums[i]
            res.append(target ^ currTotal)
        
        return res