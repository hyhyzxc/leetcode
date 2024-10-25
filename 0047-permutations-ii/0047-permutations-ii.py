class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(visited, currArr):
            if len(visited) == len(nums):
                res.append(currArr)
                return
            last = None
            for i in range(len(nums)):
                if i not in visited and nums[i] != last:
                    visited.add(i)
                    currArr.append(nums[i])
                    backtrack(visited.copy(), currArr.copy())

                    visited.remove(i)
                    currArr.pop()

                    last = nums[i]
            
        backtrack(set(), [])
        return res
                    