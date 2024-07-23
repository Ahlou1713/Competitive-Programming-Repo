class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []

        for a,b in costs:
            diffs.append([b-a,a,b])
        
        diffs.sort()
        res = 0

        for i in range(len(diffs)):
            if i < len(diffs) / 2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]
        return res


        


        