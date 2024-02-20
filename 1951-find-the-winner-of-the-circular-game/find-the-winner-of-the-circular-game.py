class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n+1)]
        start = 0
        while len(friends) > 1:
            to_be_removed = (start + k - 1)%len(friends)
            friends.pop(to_be_removed)
            start = to_be_removed

        return friends[0]