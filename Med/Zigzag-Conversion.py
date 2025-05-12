# Solution to the ZigZag Conversion problem
# Runs in O(n) time as it does one pass through the array

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Check if len is less than numRows or its length is 1
        if numRows == 1 or len(s) <= numRows:
            return s
        
        rowString = ['' for _ in range(numRows)]

        # We switch directions when going downwards or upwards
        direction = 1
        currentRow = 0

        for character in s:
            rowString[currentRow] += character

            # Simulate going upwards and downwards in a zigzag manner
            if currentRow == 0:
                direction = 1
            elif currentRow == (numRows-1):
                direction = -1

            currentRow += direction

        result = ''
        for row in rowString:
            result += row
        return result