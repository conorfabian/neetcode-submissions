class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        prev = [-1, -1]
        for interval in intervals:
            start, end = interval
            if prev[1] < start:
                res.append(interval)
                prev = interval
            else:
                res[-1][1] = max(res[-1][1], end)

        return res
