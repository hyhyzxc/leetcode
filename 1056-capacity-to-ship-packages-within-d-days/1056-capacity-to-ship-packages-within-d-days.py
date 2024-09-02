class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def findDays(cap):
            currTotal = 0
            days = 0
            i = 0
            while i < len(weights):
                weight = weights[i]
                if currTotal + weight > cap:
                    days += 1
                    currTotal = 0
                else:
                    currTotal += weight
                    i += 1
            
            if currTotal > 0:
                days += 1
            #print(cap, days)
            return days

        l = max(weights)
        r = sum(weights)
        import math
        res = math.inf
        while l <= r:
            mid = (l + r) // 2
            if findDays(mid) > days:
                l = mid + 1
            else:
                r = mid - 1
                res = min(res, mid)
                
            
        return res
