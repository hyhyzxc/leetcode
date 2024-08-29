class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # group all stones connected to each other together
        n = len(stones)
        rank = [1 for i in range(n)]
        parent = [i for i in range(n)]
        mapRow = {}
        mapCol = {}
        for index, stone in enumerate(stones):
            r, c = stone[0], stone[1]
            if r not in mapRow:
                mapRow[r] = [index]
            else:
                mapRow[r].append(index)
            
            if c not in mapCol:
                mapCol[c] = [index]
            else:
                mapCol[c].append(index)

        def find(i):
          
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        
        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
        
        for group in mapRow.values():
            if len(group) > 1:
                first = group[0]
                for j in group[1:]:
                    union(first, j)
        
        for group in mapCol.values():
            if len(group) > 1:
                first = group[0]
                for j in group[1:]:
                    union(first, j)
        
        hashSet = set()
        for i in range(n):
            parent[i] = find(i)
            hashSet.add(parent[i])
        
        return len(stones) - len(hashSet)