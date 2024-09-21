import math
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def checkValid(days):
            res = 0
            i = 0
            count = 0
            while i < len(bloomDay):
                if bloomDay[i] <= days:
                    count += 1
                
                    if count >= k:
                        res += 1
                        count = 0
                else:
                    if count >= k:
                        res += 1
                        count = 0
                    else:
                        count = 0
                i += 1
            if res >= m:
                return True
            else:
                return False

        l = 1
        r = max(bloomDay)

        res = r + 1
        while l <= r:
            mid = l + (r-l) // 2
            if checkValid(mid):
                print(mid)
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        if res > max(bloomDay):
            return -1
        else:
            return res
