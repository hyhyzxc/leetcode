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
            j = sum(arr)
            if j == target:
                res.append(arr.copy())
                return
            elif j > target or i >= len(candidates):
                return
            else:
                # case 1: repeat my current index
                arr.append(candidates[i])
                backtrack(arr, i)
                # case 2: move on to next index
                arr.pop()
                backtrack(arr, i+1)
        
        backtrack([], 0)
        return res
            