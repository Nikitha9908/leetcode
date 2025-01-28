class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0  # Pointer to the last unique element's index
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # When we find a new unique element
                i += 1
                nums[i] = nums[j]
        
        return i + 1  # The number of unique elements


# Now, create an instance of the Solution class and use the method
solution = Solution()
nums = [1, 1, 2]
k = solution.removeDuplicates(nums)
print(k)  # Output: 2
print(nums[:k])  # Output: [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = solution.removeDuplicates(nums)
print(k)  # Output: 5
print(nums[:k])  # Output: [0, 1, 2, 3, 4]
