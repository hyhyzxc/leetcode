class Solution:
    def compressedString(self, word: str) -> str:
        res = ""
        currLetter = word[0]
        currCount = 1
        for i in range(1, len(word)):
            if word[i] == currLetter:
                currCount += 1
                if currCount > 9:
                    res += str(9) + currLetter
                    currCount = 1
                    
            else:
                res += str(currCount) + currLetter
                currLetter = word[i]
                currCount = 1
        
        res += str(currCount) + currLetter
        return res