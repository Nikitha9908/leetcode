class Solution:
    def combinationSum2(self, candidates, target):
        # Sort the candidates to handle duplicates and improve efficiency
        candidates.sort()
        result = []
        
        # Backtracking helper function
        def backtrack(start, target, current_combination):
            if target == 0:  # If we reach the target, we found a valid combination
                result.append(list(current_combination))
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the current number is greater than the target, no point in continuing
                if candidates[i] > target:
                    break
                # Include the current number and recurse
                current_combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current_combination)
                # Backtrack, remove the last number
                current_combination.pop()
        
        # Start backtracking from the first index
        backtrack(0, target, [])
        return result
