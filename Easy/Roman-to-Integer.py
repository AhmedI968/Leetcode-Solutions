# LeetCode Roman to Integer
# My approach is to use a dictionary to map Roman numerals to their integer values.
# I iterate through the string and for each character, I check if the current character is larger than the previous one.
# If it is, I subtract the value of the previous character from the result and add the value of the current character.
# If it is not, I simply add the value of the current character to the result.
# This is because in Roman numerals, if a smaller numeral appears before a larger one, it is subtracted (e.g., IV = 4).
# The time complexity of this solution is O(n) and the space complexity is O(1).

class Solution:
    def romanToInt(self, s: str) -> int:
        # Use a dict for easy access
        romanVals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Intialize the value
        res = 0

        for i in range(len(s)):
            # Check if the current symbol larger than the prev which implies a IV = 4 situation
            if i > 0 and romanVals[s[i]] > romanVals[s[i - 1]]:
                res += romanVals[s[i]] - (2 * romanVals[s[i - 1]])
            else:
                res += romanVals[s[i]]
        
        return res