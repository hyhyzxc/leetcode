class Solution:
    def minimumSteps(self, s: str) -> int:
        head = 0
        while head < len(s) and s[head] == '0':
            head += 1
        
        res = 0

        ptr = head
        while ptr < len(s):
            if s[ptr] == '0':
                res += ptr - head
                head += 1
            ptr += 1
        
        return res