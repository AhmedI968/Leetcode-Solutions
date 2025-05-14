# Solution to the problem "String to Integer (atoi)" on LeetCode.
# This function converts a string to an integer, following the rules of the atoi function.
# It handles leading whitespace, optional sign, and numeric characters.
# It also checks for overflow and underflow conditions, returning the appropriate limits.

class Solution:
    def myAtoi(self, s: str) -> int:

        sign = 1
        index = 0
        res = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Go through whitespaces
        while index < len(s) and s[index] == ' ':
            index += 1
        
        # Check for sign
        if index < len(s) and (s[index] == "-" or s[index] == "+"):
            sign = -1 if s[index] == "-" else 1
            index += 1
        
        # Find digits
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])

            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            res = (res * 10) + digit
            index += 1

        return sign * res
