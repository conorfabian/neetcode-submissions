class MedianFinder:

    def __init__(self):
        self.median = []
        

    def addNum(self, num: int) -> None:
        self.median.append(num)
        self.median.sort()
        

    def findMedian(self) -> float:
        medianIdx = len(self.median) // 2

        if len(self.median) % 2 == 0:
            return (self.median[medianIdx] + self.median[medianIdx - 1]) / 2
        else:
            return self.median[medianIdx]