from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Create a default dictionary where each key maps to a list
        anagram_groups = defaultdict(list)
        
        # Iterate through each string in the input list
        for s in strs:
            # Sort the string and use it as a key
            sorted_str = ''.join(sorted(s))
            # Append the original string to the corresponding anagram group
            anagram_groups[sorted_str].append(s)
        
        # Return the values (which are lists of anagrams)
        return list(anagram_groups.values())
