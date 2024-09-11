class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        #1010
        #0111
        s1 = bin(start)[2:]
        s2 = bin(goal)[2:]
        
        length = max(len(s1) , len(s2))
        s1 = s1.zfill(length)
        s2 = s2.zfill(length)
        #print(s1, s2)
        for b1, b2 in zip(s1, s2):
            res += int(b1) ^ int(b2)
        return res