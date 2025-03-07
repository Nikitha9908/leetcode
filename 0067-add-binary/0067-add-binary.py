class Solution:
    def addBinary(self, a, b):  # Removed type hints
        return bin(int(a, 2) + int(b, 2))[2:]

# Example usage
sol = Solution()
print(sol.addBinary("11", "1"))     # Output: "100"
print(sol.addBinary("1010", "1011"))  # Output: "10101"
