from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque([])
        res = float("inf")
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            if curr_sum >= k:
                res = min(res, r+1)
            while q and curr_sum - q[0][0] >= k:
                prefix, end_index = q.popleft()
                res = min(res, r - end_index)
            while q and curr_sum <= q[-1][0]:
                q.pop()
            q.append((curr_sum, r))
        return res if res != float("inf") else -1