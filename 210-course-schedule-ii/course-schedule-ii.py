class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order = []

        for a, b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1

        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            order.append(course)


            for neighbour in graph[course]:

                incoming[neighbour] -= 1

                if incoming[neighbour] == 0:
                    queue.append(neighbour)


        if len(order) != numCourses:
            return []


        return order
