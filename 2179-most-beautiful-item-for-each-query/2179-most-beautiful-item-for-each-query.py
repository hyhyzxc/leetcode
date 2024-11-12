class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: x[0])
        res = []
        max_till_here = []
        curr_max = 0
        for i in range(len(items)):
            curr_max = max(curr_max, items[i][1])
            max_till_here.append(curr_max)

        def binary_search(n, target):
            l = 0
            r = len(n) - 1
            while l <= r:
                mid = (l+r) // 2
                if n[mid][0] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        for max_price in queries:
            max_index = binary_search(items, max_price)
            res.append(max_till_here[max_index-1]) if max_index > 0 else res.append(0)
        return res