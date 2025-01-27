class Solution:
    def reverse(self, x):
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle the negative case
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits of x
        reversed_x = int(str(x)[::-1])
        
        # Reapply the sign to the reversed number
        reversed_x *= sign
        
        # Check for overflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
