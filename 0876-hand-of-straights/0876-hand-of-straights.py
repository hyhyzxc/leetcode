import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = {}
        for i in hand:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        
        heap = list(counts.keys())
        group = [0] * groupSize
        heapq.heapify(heap)
        while heap:
            curr = heap[0]
            for i in range(curr, curr+groupSize):
                if i not in counts or counts[i] == 0:
                    return False
                else:
                    counts[i] -= 1
                    if counts[i] == 0:
                        if i != heap[0]:
                            return False
                        heapq.heappop(heap)
        return True

