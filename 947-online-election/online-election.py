from collections import Counter

class TopVotedCandidate(Counter):

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

    def q(self, t: int) -> int:
        
        def returnPosition(self, t: int) -> int:
            left = 0
            right = len(self.times)

            while left < right:
                mid = left + (right-left) // 2

                if self.times[mid] == t:
                    return mid
                elif self.times[mid] > t:
                    right = mid
                else:
                    left = mid + 1

            return left-1

        j = returnPosition(self, t)
        persons_ = self.persons[:j+1]
        persons_counter = Counter(persons_)

        max_count = max(persons_counter.values())
        most_common_persons = [key for key, value in persons_counter.items() if value == max_count]
        
        if len(most_common_persons) == 1:
            return most_common_persons[0]
        else:
            most_recent_person = None
            for person in reversed(persons_):
                if person in most_common_persons:
                    most_recent_person = person
                    break
            return most_recent_person


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)