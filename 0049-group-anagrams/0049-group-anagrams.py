from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Create a dictionary to store groups of anagrams
        anagrams = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            # Sort the string and use the sorted string as the key
            sorted_str = ''.join(sorted(s))
            # Append the original string to the corresponding anagram group
            anagrams[sorted_str].append(s)
        
        # Return the values of the dictionary, which are the anagram groups
        return list(anagrams.values())

# Example test cases
sol = Solution()

# Test case 1
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) 
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Test case 2
print(sol.groupAnagrams([""])) 
# Output: [['']]

# Test case 3
print(sol.groupAnagrams(["a"])) 
# Output: [['a']]
