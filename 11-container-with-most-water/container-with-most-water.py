class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        left = 0
        right = n-1

        while left<right:
            curr_area = (right-left) * min(height[left], height[right])
            area = max(area, curr_area)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return area