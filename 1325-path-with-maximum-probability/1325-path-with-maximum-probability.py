import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = [{} for i in range(n)]
        for edge, prob in zip(edges, succProb):
            n1, n2 = edge[0], edge[1]
            adjList[n1][n2] = prob
            adjList[n2][n1] = prob
        
        pq = [(-1, start_node)]
        visit = set()
        while pq:
            cost, curr = heapq.heappop(pq)
            visit.add(curr)
            if curr == end_node:
                return cost * -1
            else:
                for neighbor, prob in adjList[curr].items():
                    if neighbor not in visit:
                        heapq.heappush(pq, (cost * prob, neighbor))
        return 0
            