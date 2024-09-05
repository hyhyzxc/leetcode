class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
     
        def binarySearch(spell):
            l = 0
            r = len(potions) - 1
            while l <= r:
                mid = (l+r) // 2
                if spell * potions[mid] >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        for spell in spells:
            last_fail = binarySearch(spell)
            #print(last_fail)
            res.append(len(potions) - last_fail)
        return res