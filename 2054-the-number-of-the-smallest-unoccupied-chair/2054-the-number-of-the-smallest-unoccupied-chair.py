import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(t[0], t[1], i) for i,t in enumerate(times)]

        times.sort(key = lambda x:x[0])
        available = [i for i in range(len(times))]
        used = []

        for start, end, i in times:
           

            while used and used[0][0] <= start:
                leave, chair = heapq.heappop(used)
                heapq.heappush(available, chair)
            
            chair = heapq.heappop(available)
            heapq.heappush(used, (end, chair))
            if i == targetFriend:
                return chair
