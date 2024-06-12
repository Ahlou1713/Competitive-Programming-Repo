class Solution:
     def findCenter(self, edges: List[List[int]]) -> int:
        ed = defaultdict(list)
        for i in edges:
            ed[i[0]].append(i[1])
            ed[i[1]].append(i[0])
            
        n = len(ed)

        for i, j in ed.items():
            if len(j) == n-1:
                return i
        