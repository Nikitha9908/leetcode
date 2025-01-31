class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n:
            if n % 2:  # If n is odd
                result *= x
            x *= x  # Square the base
            n //= 2  # Reduce exponent by half
        
        return result

# Example Usage
solution = Solution()
print(solution.myPow(2.00000, 10))  # Output: 1024.00000
print(solution.myPow(2.10000, 3))   # Output: 9.26100
print(solution.myPow(2.00000, -2))  # Output: 0.25000
