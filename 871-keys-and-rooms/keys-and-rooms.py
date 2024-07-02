class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)

        n = len(rooms)

        for i in range(n):
            graph[i] = rooms[i]

        print(graph)
        visited = []
        queue = deque([0])
        save = [0]

        while queue:
            node = queue.popleft()

            if node not in visited:
                visited.append(node)

                for neighbour in graph[node]:
                    queue.append(neighbour)
                    if neighbour != node:
                        save.append(neighbour)

        for key in range(n):
            if key not in save:
                return False

        
        return True