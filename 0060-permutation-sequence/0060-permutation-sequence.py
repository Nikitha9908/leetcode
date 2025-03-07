import math

class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))  # List of numbers to pick from
        k -= 1  # Convert k to zero-based index
        result = []
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)  # Factorial of remaining elements
            index = k // fact  # Find the correct digit
            result.append(str(numbers.pop(index)))  # Remove from list
            k %= fact  # Update k for next position

        return "".join(result)

# Example usage
sol = Solution()
print(sol.getPermutation(3, 3))  # Output: "213"
print(sol.getPermutation(4, 9))  # Output: "2314"
print(sol.getPermutation(3, 1))  # Output: "123"
