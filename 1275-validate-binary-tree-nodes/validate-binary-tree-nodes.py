class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * n
        
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])
                indegree[rightChild[i]] += 1
        
        root = -1
        for i in range(n):
            if indegree[i] == 0:
                if root != -1:
                    return False  
                root = i
        
        if root == -1:
            return False  

        queue = deque([root])
        visited = set(queue)
        
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if neighbour in visited:
                    return False  
                visited.add(neighbour)
                queue.append(neighbour)
        
        return len(visited) == n
