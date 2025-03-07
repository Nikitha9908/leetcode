import re

class Solution:
    def isNumber(self, s):
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return bool(re.match(pattern, s.strip()))

# Example test cases
sol = Solution()
print(sol.isNumber("0"))  # True
print(sol.isNumber("e"))  # False
print(sol.isNumber("."))  # False
print(sol.isNumber("2e10"))  # True
print(sol.isNumber("53.5e93"))  # True
print(sol.isNumber("99e2.5"))  # False
