class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(1, len(s)):
            newStr = s[i:] + s[:i]
            if newStr == goal:
                return True
        return s == goal