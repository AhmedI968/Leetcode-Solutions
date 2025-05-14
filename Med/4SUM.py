# Solution to the 4SUM problem on LeetCode
# My approach is to use a similar technique to the 3SUM problem, but with an additional loop for the fourth number.
# The idea is to sort the input list and then use two pointers to find the other two numbers that sum up to the target.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Similar idea to 3SUM just use an extra loop for the fourth index
        nums.sort()
        result = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return result