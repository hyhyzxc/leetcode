from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        def bfs(i):

            if visited[i]:
                return True
            queue = deque([i])
            visited[i] = 1
            while queue:
                j = queue.popleft()
                for neighbour in graph[j]:
                    if visited[neighbour] == visited[j]:
                        return False
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = visited[j] * -1
                    
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True