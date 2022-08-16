class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        self.l.sort()

        mid = len(self.l)//2
        
        if len(self.l) % 2 != 0:
            return self.l[mid]
        else:
            return (self.l[mid-1]+self.l[mid])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()