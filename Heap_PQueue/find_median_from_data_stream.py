# leetcode 295
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. 

# using a simple insertion sort algo gets time limit exceeded. Can't do that
# use two heaps, a small heap and a large heap, every number in small heap is smaller than any number in large heap.
# the two heaps will be approximately equal. ex: 2 elements in small heap 2 in large heap, offset of 1 is allowed for even numbers
# adding an element to heap is o(logn), removing is also o(logn)
# finding a max in a heap is always o(1) 

# small heap will be represented as a MAX heap, large heap will be represented as a MIN heap.
# get small heap max o(1) get max heap min o(1) add them together and divide by 2 to get the median.
# ex: small heap = [1,2] large heap = [3,4], o(1) operation to get the values we need. Only works if size is approx equal
# with odd numbers, we want to take the value of the heap with the odd value.

class MedianFinder:

    def __init__(self):
        # initialize two heaps,small heap & large heap
        # every element in small heap is smaller than every element in large heap
        # small heap will be a max heap
        # large heap will be a min heap
        # heaps should be approx equal in size
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # always adding to small heap first then balance later
        # python heap is only a min heap so in order to use small as a max heap,
        # multiply every number by -1
        heapq.heappush(self.small, -1 * num)

        #ensure every element in small is <= large heap
        if (self.small and self.large and 
        (-1 * self.small[0]) > self.large[0]): # get the top of the heap as the zeroith index
            value = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        #check if the sizes of each heap are uneven and balance them
        if len(self.small) > len(self.large) +1: # difference is 2 or greater, not allowed
            value = -1* heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        if len(self.large) > len(self.small) +1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * value)
        

    def findMedian(self) -> float:
        # check if there is an odd length, return index zero of the odd length heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + (self.large[0])) / 2 
 