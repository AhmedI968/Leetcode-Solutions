# LeetCode Problem: Three Sum
# My approach is to use a two-pointer technique to find all unique triplets in the array that sum up to zero.
# The idea is to sort the array first, and then iterate through the array with a fixed pointer.
# For each fixed pointer, we use two pointers to find the other two numbers that sum up to zero.
# We also need to handle duplicates to avoid counting the same triplet multiple times.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Intialize the two pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return result