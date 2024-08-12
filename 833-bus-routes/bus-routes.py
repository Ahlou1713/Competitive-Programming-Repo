class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0

        ways = defaultdict(set)

        for bus, stops in enumerate(routes):
            for stop in stops:
                ways[stop].add(bus)

        queue = deque(ways[target])
        output = 0
        visited = set()

        while queue:
            output += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                if source in routes[node]:
                    return output
                queue.extend(bus for location in routes[node] for bus in ways[location] if bus not in visited)

        return -1


                

        