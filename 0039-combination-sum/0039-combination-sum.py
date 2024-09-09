class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #[2,3,6,7]
        #[2],[2,2],[2,2,2,],[2,2,2,2]

        # case 1: repeat my current index

        # case 2: move on to next index

        #terminating conditions: 
        #1) sum exceeds target -> false
        #2) sum == target -> true

        res = []

        def backtrack(arr, i):
            if sum(arr) == target:
                res.append(arr)
                return
            elif sum(arr) > target or i >= len(candidates):
                return
            else:
                # case 1: repeat my current index
                arr.append(candidates[i])
                backtrack(arr.copy(), i)
                # case 2: move on to next index
                arr.pop()
                backtrack(arr.copy(), i+1)
        
        backtrack([], 0)
        return res
            