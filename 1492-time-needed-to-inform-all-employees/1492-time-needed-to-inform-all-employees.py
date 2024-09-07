from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                adjList[manager[i]].append(i)
        stack = [(headID, informTime[headID])]
        res = 0
        visited = set()
        def dfs(curr):
            time = 0
            visited.add(curr)
            for neighbour in adjList[curr]:
                if neighbour not in visited:
                    time = max(time, dfs(neighbour))
            time += informTime[curr]
            return time
        return dfs(headID)
