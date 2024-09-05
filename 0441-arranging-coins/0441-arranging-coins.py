class Solution:
    def arrangeCoins(self, n: int) -> int:
        # sum = k/2 (2a + (k-1)*d)
        # sum = k/2 (2 + (k-1))
        # sum = k + k^2/2 - k/2
        # sum = k^2/2 + k/2

        l = 0
        r = n

        while l <= r:
            mid = (l + r) // 2
            total = ((mid**2) / 2) + (mid / 2)
            #print(mid, total)
            if total == n:
                return mid
            elif total < n:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1