class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = [0] * n

        for a, b in roads:
            graph[a] += 1
            graph[b] += 1

        max_network_rank = 0

        for i in range(n):
            for j in range(i+1, n):
                if [i,j] in roads or [j,i] in roads:
                    network_rank = graph[i] + graph[j] - 1
                else:
                    network_rank = graph[i] + graph[j]
                max_network_rank = max(max_network_rank, network_rank)


        return max_network_rank 


        