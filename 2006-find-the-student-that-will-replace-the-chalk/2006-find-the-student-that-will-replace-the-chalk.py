class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        remaining = k % sum(chalk)
        if remaining == 0:
            return 0
        else:
            for i in range(len(chalk)):
                remaining -= chalk[i]
                if remaining < 0:
                    return i
        
                
