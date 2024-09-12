class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashSet = set(i for i in allowed)
        res = 0
        for word in words:
            for letter in word:
                if letter not in hashSet:
                    res -= 1
                    break
            res += 1
        return res