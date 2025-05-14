# LeetCode Problem: Container With Most Water
# My approach is to use a two-pointer technique to find the maximum area of water that can be contained between two lines.
# The idea is to start with two pointers, one at the beginning and one at the end of the height array.
# We calculate the area formed between the two lines and move the pointer pointing to the shorter line towards the other pointer.
# This is because the area is limited by the shorter line, and moving the pointer pointing to the taller line will not increase the area.
# We repeat this process until the two pointers meet.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            max_area = max(max_area, (right - left)*(min(height[left], height[right])))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area