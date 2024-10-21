class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        l = r = 0
        res = [0]
        
        def backtrack(i, used):
            
            if i >= len(s):
                res[0] = max(res[0], len(used))
                return True
            
            r = i
            while r < len(s) and s[i:r+1] in used:
                r += 1
            
            if r >= len(s):
                return False
            
           
            while True:
                used.add(s[i:r+1])
                if not backtrack(r+1, used.copy()):
                    used.remove(s[i:r+1])
                    r += 1
                else:
                    break
            
        backtrack(0, set())
        return res[0]
            
