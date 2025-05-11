# Solution to the Two Sum problem
# Problem link: https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# What I did was to create a dictionary that stores the indices of each number in the array.
# Then, for each number in the array, I check if the complement/reminder (target - number) exists in the dictionary.
# If it does, I check if the index of the complement/reminder is not equal to the current index.
# If both conditions are satisfied, I return the indices of the two numbers.
# If the loop completes without finding a solution, I return an empty list.
# The time complexity of this solution is O(n) and the space complexity is also O(n).

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisdict = {}
        for i in range(len(nums)):
            if nums[i] not in thisdict:
                thisdict[nums[i]] = []
            thisdict[nums[i]].append(i)
        
        for j in range(len(nums)):
            rem = target - nums[j]
            if rem in thisdict:
                for index in thisdict[rem]:
                    if index != j:
                        return [j, index]

        return []