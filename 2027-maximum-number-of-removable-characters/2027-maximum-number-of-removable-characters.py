class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubsequence(a, b):
            # check if b is subsequence of a
            i,j = 0, 0
            while i < len(a):
                if a[i] == b[j]:
                    j += 1
                    if j == len(b):
                        return True
                i += 1
            return False
        
        l = 1
        r = len(removable)
        res = 0
        while l <= r:
            mid = l + (r-l) // 2
            remov = set(removable[:mid])
            currStr = ""
            for i in range(len(s)):
                if i not in remov:
                    currStr += s[i]
            if isSubsequence(currStr, p):
                res = max(mid, res)
                l = mid + 1
            else:
                r = mid - 1
        return res
