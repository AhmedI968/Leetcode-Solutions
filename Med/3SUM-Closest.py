# Solution for the 3SUM Closest problem on LeetCode.
# My approach is to sort the input list and then use a two-pointer technique to find the closest sum of three numbers to the target.
# The idea is to fix one number and then use two pointers to find the other two numbers that sum up to the target.
# We also need to handle duplicates to avoid counting the same triplet multiple times.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = float('inf')

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest