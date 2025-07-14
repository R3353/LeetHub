from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1) dictionary, 2) heapq; sort by value in desc order; 3) return first k keys.
        dict = defaultdict(int) #defaultdict makes sure every key has a value. default val = 0
        for n in nums:
            dict[n] += 1
        heap = [] #keep a heap of size k. heap auto sorts!
        for num, instances in dict.items():
            if len(heap) < k or instances > heap[0][0]:
                heapq.heappush(heap, [instances, num])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]