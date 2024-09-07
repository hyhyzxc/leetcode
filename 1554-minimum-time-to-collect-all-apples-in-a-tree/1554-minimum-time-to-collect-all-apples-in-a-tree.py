class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # at every node run dfs, if no apple return 0, if find apple return count
        adjList = collections.defaultdict(list)
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        visited = set()
        #print(adjList)
        def dfs(curr, time):
            #print(curr, time)
            visited.add(curr)
            if curr == None:
                return (False, 0)
            foundApple = hasApple[curr]
            for neighbour in adjList[curr]:
                #print(neighbour)
                if neighbour not in visited:
                    apple, timing = dfs(neighbour, 2)
                    #print(neighbour, apple, timing)
                    visited.add(neighbour)
                    if apple:
                        time += timing
                        #print(curr, neighbour, timing)
                        foundApple = True
            if not foundApple:
                return (False, 0)
            else:
                return (True, time)
                
        return dfs(0, 0)[1]