class Solution:
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # Return early if no carry needed
            digits[i] = 0  # If digit is 9, set to 0 and continue

        # If all were 9s, we need to add a leading 1
        return [1] + digits

# Example test cases
sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(sol.plusOne([9]))  # Output: [1,0]
print(sol.plusOne([9,9,9]))  # Output: [1,0,0,0]
