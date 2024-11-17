import heapq
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = [] #store (prefix, end_index)
        r = 0
        the_sum = 0
        res = float("inf")
        while r < len(nums):
            the_sum += nums[r]
            if the_sum >= k:
                res = min(res, r+1)
            while heap and the_sum - heap[0][0] >= k:
                prefix, end_index = heapq.heappop(heap)
                res = min(res, r - end_index)
            
            heapq.heappush(heap, (the_sum, r))
            r += 1

        return res if res != float("inf") else -1