class Solution:
    def permute(self, nums):
        result = []
        
        def backtrack(path, remaining):
            # Base case: if no remaining elements, add the path to the result
            if not remaining:
                result.append(path)
                return
            
            # Recursive case: try each element in the remaining list
            for i in range(len(remaining)):
                # Take the current element and recurse with the rest
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        # Start the backtracking with an empty path and the full list of numbers
        backtrack([], nums)
        return result

# Example test cases
sol = Solution()
print(sol.permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(sol.permute([0, 1]))     # Output: [[0, 1], [1, 0]]
print(sol.permute([1]))        # Output: [[1]]
