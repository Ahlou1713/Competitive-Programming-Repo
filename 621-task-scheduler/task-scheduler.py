class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)

        max_heap = [(-value, key) for key, value in dic.items()]
        heapify(max_heap)
        queue = deque()
        time = 0

        while max_heap or queue:
            if max_heap:
                freq, task = heappop(max_heap)
                if freq+1:
                    queue.append((freq+1, task, time))
            if queue:
                if time - queue[0][2] >= n:
                    freq, task, _ = queue.popleft()
                    heappush(max_heap, (freq, task))

            time += 1

        return time