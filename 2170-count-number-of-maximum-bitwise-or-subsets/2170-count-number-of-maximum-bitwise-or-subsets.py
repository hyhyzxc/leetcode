class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = [0]
        currMax = [0]
        
        def backtrack(i, currSum):
            if i == len(nums):
                return
            prevSum = currSum
            currSum = currSum | nums[i]
            if currSum > currMax[0]:
                currMax[0] = currSum
                res[0] = 1
            elif currSum == currMax[0]:
                res[0] += 1

            backtrack(i+1, currSum)
            backtrack(i+1, prevSum)
        
        backtrack(0, 0)
        return res[0]

                