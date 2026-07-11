class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most_water = 0

        while left < right:
            width = right - left
            water_height = min(heights[left], heights[right])
            area = width * water_height
            most_water = max(most_water, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return most_water

