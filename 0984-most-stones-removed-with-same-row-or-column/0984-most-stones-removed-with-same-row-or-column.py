class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # group all stones connected to each other together
        mapRow = {}
        mapCol = {}
        N = len(stones)
        for i in range(N):
            stone = stones[i]
            r, c = stone[0], stone[1]
            if r not in mapRow:
                mapRow[r] = [i]
            else:
                mapRow[r].append(i)
            if c not in mapCol:
                mapCol[c] = [i]
            else:
                mapCol[c].append(i)
        
        parent = [i for i in range(N)]
        rank = [1 for i in range(N)]
        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        def union(a, b):
            pA, pB = find(a), find(b)
            if pA == pB:
                return
            if rank[pA] > rank[pB]:
                rank[pA] += rank[pB]
                parent[pB] = pA
            else:
                rank[pB] += rank[pA]
                parent[pA] = pB
        for group in mapRow.values():
            start = group[0]
            for i in range(1, len(group)):
                union(start, group[i])
        for group in mapCol.values():
            start = group[0]
            for i in range(1, len(group)):
                union(start, group[i])
        hashSet = set()
        for i in range(N):
            parent[i] = find(i) 
            hashSet.add(parent[i])
        return N - len(hashSet)   

        # find number of connected components

        # return numStones - numComponents