# Solution to the Longest Substring Without Repeating Characters problem
# Problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest substring without repeating characters.
# What I did was to use a sliding window approach with a dictionary to keep track of the last seen index of each character.
# I maintain a variable start to keep track of the start index of the current substring.
# As I iterate through the string, if I encounter a character that is already in the dictionary and its last seen index is greater than or equal to start,
# I update start to the last seen index + 1.
# I then update the last seen index of the character to the current index.
# Finally, I calculate the length of the current substring and update maxLength if it is greater than the previous maxLength.
# The time complexity of this solution is O(n), where n is the length of the string.
# Runtime was 15ms beating 82.04% of the submissions.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        start = 0
        charIndex = {}

        for i, char in enumerate(s):
            if char in charIndex and charIndex[char] >= start:
                start = charIndex[char] + 1
            charIndex[char] = i
            maxLength = max(maxLength, i - start + 1)
        
        return maxLength