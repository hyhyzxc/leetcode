class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        queue = deque([('0000', 0)])
        visited = set(deadends)
        if '0000' in visited:
            return -1
        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns+1))
        return -1