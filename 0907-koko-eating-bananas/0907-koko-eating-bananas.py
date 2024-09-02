import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getTime(h):
            res = 0
            for pile in piles:
                res += math.ceil(pile / h)
            return res
        
        piles.sort()
        l = 1
        r = piles[-1]
        while l <= r:
            mid = (l + r) // 2
            if getTime(mid) <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l