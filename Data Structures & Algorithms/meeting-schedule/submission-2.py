"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        prevEnd = None
        for interval in intervals:
            start, end = interval.start, interval.end
            if not prevEnd or start >= prevEnd:
                prevEnd = end
            else:
                return False

        return True