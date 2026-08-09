class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = maxRight = 0
        left, right = 0, len(height) - 1
        water = 0

        while left < right:
            if height[left] <= height[right]:
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]
                right -= 1
        
        return water