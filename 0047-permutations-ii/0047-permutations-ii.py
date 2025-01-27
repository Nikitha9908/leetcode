class Solution:
    def permuteUnique(self, nums):
        result = []
        nums.sort()  # Sort the input to handle duplicates easily
        
        def backtrack(path, used):
            # Base case: if the path has the same length as nums, it's a valid permutation
            if len(path) == len(nums):
                result.append(path[:])  # Append a copy of the current path
                return
            
            for i in range(len(nums)):
                # Skip the used elements or duplicates (check adjacent duplicates)
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                
                # Choose the current element and recurse
                used[i] = True
                backtrack(path + [nums[i]], used)
                used[i] = False  # Backtrack
                
        used = [False] * len(nums)  # To track the usage of elements
        backtrack([], used)
        return result

# Example test cases
sol = Solution()
print(sol.permuteUnique([1, 1, 2]))  # Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
print(sol.permuteUnique([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
