from collections import Counter

class Solution:
    def permuteUnique(self, nums):
        def backtrack(path, counter):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[num] += 1
        
        result = []
        counter = Counter(nums)
        backtrack([], counter)
        return result

# Example Usage
solution = Solution()
nums1 = [1,1,2]
nums2 = [1,2,3]
print(solution.permuteUnique(nums1))
print(solution.permuteUnique(nums2))
