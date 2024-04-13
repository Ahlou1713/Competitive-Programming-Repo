class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        n = len(people)
        left = 0
        right = n-1
        output = 0
        while left<=right:
            if people[left]+people[right] <= limit:
                left+=1
            right-=1
            output+=1

        return output