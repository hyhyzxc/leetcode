class Solution:
    def maximumSwap(self, num: int) -> int:
        res = num
        increase = 0

        num = str(num)
        length = len(num)
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                current = int(num[i]) * 10 ** (length - i - 1) + int(num[j]) * 10 ** (length-j-1)
                swapped = int(num[j]) * 10 ** (length-i-1) + int(num[i])*10**(length-j-1)
                if swapped-current > increase:
                    increase = swapped-current
                    res = int(num[0:i] + num[j] + num[i+1:j] + num[i] + num[j+1:])
        return res
                