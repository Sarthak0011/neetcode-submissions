class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash = [0] * 26
        for task in tasks:
            hash[ord(task) - ord('A')] += 1
        
        max_heap = []
        for count in hash:
            if count: max_heap.append(-count)
        heapq.heapify(max_heap)

        q = deque()
        time = 0
        while max_heap or q:
            time += 1
            if max_heap:
                task = -(heapq.heappop(max_heap)) - 1
                if task:
                    q.append([-task, time+n])
            
            if q:
                if time >= q[0][1]:
                    task, exec_time = q.popleft()
                    heapq.heappush(max_heap, task)
        return time