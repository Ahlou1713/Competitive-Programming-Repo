class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target_ = tuple(map(int, target))

        moves = [(1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0), 
                 (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)]
        
        result = (0,0,0,0)

        if result == target_:
            return 0

        deadends_set = {tuple(map(int, deadend)) for deadend in deadends}

        if result in deadends_set:
            return -1

        queue = deque([(result, 0)])
        visited = set([result])

        while queue:
            node, weight = queue.popleft()
            
            for move in moves:
                next_position = tuple((node[i] + move[i]) % 10 for i in range(4))

                if next_position in deadends_set or next_position in visited:
                    continue

                if next_position == target_:
                    return weight + 1
                    
                visited.add(next_position)
                queue.append((next_position, weight + 1))

        return -1