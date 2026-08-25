class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort()
        prev = []
        for i in range(len(intervals)):
            if prev and prev[1] >= intervals[i][0]:
                prev = [min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])]
            else:
                if prev: res.append(prev)
                prev = intervals[i]

        res.append(prev)
        return res