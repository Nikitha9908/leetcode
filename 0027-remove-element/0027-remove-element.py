class Solution:
    def removeElement(self, nums, val):
        j = 0  # Pointer to track the position of the next valid element
        
        for i in range(len(nums)):
            if nums[i] != val:  # If the current element is not equal to val
                nums[j] = nums[i]  # Move it to the "valid" position
                j += 1  # Increment the valid position
        
        return j  # The number of elements that are not equal to val
