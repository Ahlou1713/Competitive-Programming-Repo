class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def findHeater(house: int, heaters: List[int]):
            left = 0
            right = len(heaters) - 1
            radius = float('+inf')
            while left <= right:
                mid = left + (right-left) // 2
                radius = min(radius, abs(house-heaters[mid]))

                if house < heaters[mid]:
                    right = mid - 1
                elif house > heaters[mid]:
                    left = mid + 1
                else:
                    break

            return radius

        radius = 0
        heaters.sort()
        for house in houses:
            radius = max(radius, findHeater(house, heaters))

        return radius

        # Shoutout to Fabrice for explaining this concept to me!