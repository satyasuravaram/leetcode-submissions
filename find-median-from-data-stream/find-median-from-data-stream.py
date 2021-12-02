import heapq
class MedianFinder:

    # Time Complexity for addNum: O(nlogn)
    # Time Complexity for findMedian: O(1)
    # Space complexity: O(n)
    
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if self.size == 0:
            heapq.heappush(self.maxHeap, -num)
        elif self.size % 2 == 0:
            if num < self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                minVal = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -minVal)
                heapq.heappush(self.minHeap, num)
        else:
            if num > -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                maxVal = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, maxVal)
                heapq.heappush(self.maxHeap, -num)
        self.size += 1

    def findMedian(self) -> float:
        if self.size % 2 == 1:
            return -self.maxHeap[0]
        return (self.minHeap[0] - self.maxHeap[0]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()