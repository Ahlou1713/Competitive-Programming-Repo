class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        start, end = 0, 0
        last = defaultdict(int)

        for i, c in enumerate(s):
            last[c] = i

        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                output.append(end - start + 1)
                start = end + 1
        return output