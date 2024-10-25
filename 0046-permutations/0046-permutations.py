class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(visited, currArr):
            if len(currArr) == len(nums):
                res.append(currArr)
                return
            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    currArr.append(nums[i])
                    backtrack(visited.copy(), currArr.copy())
                    visited.remove(i)
                    currArr.pop()
        
        backtrack(set(), [])
        return res