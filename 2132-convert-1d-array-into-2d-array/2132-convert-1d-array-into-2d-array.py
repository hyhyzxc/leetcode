class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = []
        index = 0
        for i in range(m):
            curr = []
            for j in range(n):
                if index >= len(original):
                    return res
                curr.append(original[index])
                index += 1
            res.append(curr)
        return res