class Solution:
    def multiply(self, num1, num2):
        # Edge case: if either number is "0", return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize the result array with zeros
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Reverse the strings to make multiplication easier (from least significant digit)
        num1, num2 = num1[::-1], num2[::-1]
        
        # Multiply each digit and accumulate the result
        for i in range(m):
            for j in range(n):
                product = int(num1[i]) * int(num2[j])
                # Add the product to the appropriate position in the result array
                result[i + j] += product
                # Handle carry-over
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # The result array is in reverse order, so we need to reverse it
        # Convert the result array back to a string
        result_str = ''.join(map(str, result[::-1])).lstrip('0')
        
        return result_str

# Test the function
sol = Solution()
print(sol.multiply("2", "3"))  # Output: "6"
print(sol.multiply("123", "456"))  # Output: "56088"
