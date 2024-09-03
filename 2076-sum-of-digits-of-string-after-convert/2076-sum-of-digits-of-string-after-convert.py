class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        for char in s:
            res += str(ord(char) - ord('a') + 1)
        total = 0
        for _ in range(k):
            total = 0
            for i in res:
                total += int(i) 
            res = str(total)
            
        return total