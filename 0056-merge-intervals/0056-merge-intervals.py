class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda k: k[0])
        res = [intervals[0]]

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            prevStart, prevEnd = res[-1][0], res[-1][1]
            if start > prevEnd and end > prevEnd:
                res.append(interval)
            else:
                res.pop()
                res.append([min(prevStart, start), max(prevEnd, end)])
        return res