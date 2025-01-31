from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sorting ensures anagrams have the same key
            anagrams[sorted_word].append(word)

        return list(anagrams.values())

# Example Usage
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""]))  # [[""]]
print(solution.groupAnagrams(["a"]))  # [["a"]]
