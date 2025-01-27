class Solution:
    def jump(self, nums):
        n = len(nums)
        
        # Edge case: if there's only one element, no jump is needed
        if n == 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n):
            # Update the farthest point that can be reached
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the range for the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If the current_end reaches or exceeds the last index, we can stop
                if current_end >= n - 1:
                    break
        
        return jumps

# Example test cases
sol = Solution()
print(sol.jump([2, 3, 1, 1, 4]))  # Output: 2
print(sol.jump([2, 3, 0, 1, 4]))  # Output: 2
