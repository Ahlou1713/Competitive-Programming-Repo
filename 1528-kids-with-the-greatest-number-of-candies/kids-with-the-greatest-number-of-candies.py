class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)

        for i in range(len(candies)):
            candies[i] += extraCandies
            print(candies[i], max(candies))
            if candies[i] == max(candies):
                result[i] = True
            candies[i] -= extraCandies


        return result