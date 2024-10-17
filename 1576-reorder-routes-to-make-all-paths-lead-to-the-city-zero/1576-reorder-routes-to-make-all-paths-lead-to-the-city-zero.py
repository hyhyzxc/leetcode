from collections import defaultdict
import math
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list_to = defaultdict(list)
        adj_list_from = defaultdict(list)

        for connection in connections:
            start, end = connection[0], connection[1]
            adj_list_to[start].append(end)
            adj_list_from[end].append(start)
        
        queue = [0]
        visited = set()
        res = 0
        while queue:
            curr = queue.pop()
            visited.add(curr)

            for n in adj_list_to[curr]:
                if n not in visited:
                    queue.append(n)
                    res += 1
            
            for n in adj_list_from[curr]:
                if n not in visited:
                    queue.append(n)
                   
        
        return res