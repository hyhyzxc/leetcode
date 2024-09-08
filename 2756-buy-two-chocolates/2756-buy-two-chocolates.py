import math
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        choco1, choco2 = math.inf , math.inf
        for price in prices:
            if price < choco1 and price < choco2:
                drop1 = choco1 - price
                drop2 = choco2 - price
                if drop1 > drop2:
                    choco1 = price
                else:
                    choco2 = price
            elif price < choco1:
                choco1 = price
            elif price < choco2:
                choco2 = price
        if choco1 + choco2 > money:
            return money
        else:
            return money - choco1 - choco2