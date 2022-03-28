class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [-int(x) for x in nums]
        heapify(maxHeap)

        while k > 1:
            heappop(maxHeap)
            k -= 1
            
        return str(-maxHeap[0])
    # using the max heap is kind of cheating...
    # But, ok
    # Space : O(n)
    # Time: O(Nlog)