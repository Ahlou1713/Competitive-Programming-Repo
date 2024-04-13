class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        n = len(people)
        left = 0
        right = n-1
        output = 0
        while left<=right:
            curr_sum = people[left]+people[right]
            if curr_sum > limit:
                output+=1
                right-=1
            else:
                output+=1
                left+=1
                right-=1

        return output