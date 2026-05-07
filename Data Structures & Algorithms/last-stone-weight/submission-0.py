class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        while len(max_heap) > 1:
            first_heavy_stone = -heapq.heappop(max_heap)
            second_heavy_stone = -heapq.heappop(max_heap)

            if first_heavy_stone != second_heavy_stone:
                diff = abs(first_heavy_stone - second_heavy_stone)
                heapq.heappush(max_heap, -diff)
        print(max_heap)
        if not max_heap: return 0
        return -max_heap[0]