class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        ahead, behind = [], []
        heapify(ahead)
        heapify(behind)
        cost = 0

        i, j = len(costs) - 1, 0

        while j < candidates:
            heappush(ahead, costs[j])
            j += 1

        j -= 1

        while i > len(costs) - candidates - 1 and i > j:
            heappush(behind, costs[i])
            i -= 1


        pass_flag = True
        j += 1
        if j > i:
            j = i
            pass_flag = False

        while k:
            if ahead and behind:
                if ahead[0] > behind[0]:
                    cost += heapq.heappop(behind)
                    if i == j and pass_flag:
                        heapq.heappush(behind, costs[i])
                        pass_flag = False
                    elif i != j:
                        heapq.heappush(behind, costs[i])
                        i -= 1
                else:
                    cost += heapq.heappop(ahead)
                    if j == i and pass_flag:
                        heapq.heappush(ahead, costs[j])
                        pass_flag = False
                    elif j != i:
                        heapq.heappush(ahead, costs[j])
                        j += 1
            elif ahead:
                cost += heapq.heappop(ahead)
                if i > j:
                    heapq.heappush(ahead, costs[j])
                    j += 1
            elif behind:
                cost += heapq.heappop(behind)
                if i > j:
                    heapq.heappush(behind, costs[i])
                    i -= 1
            k -= 1

        return cost