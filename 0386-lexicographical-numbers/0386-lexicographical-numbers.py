class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        order = [0,1,2,3,4,5,6,7,8,9]
        res = []

        def dfs(i, curr):
            if curr <= n:
                res.append(curr)
            else:
                return
            
            curr = str(curr)
            for num in order:
                curr += str(num)
                dfs(i, int(curr))
                curr = curr[:-1]
        
        for i in range(1, 10):
            dfs(i, i)
        
        return res
