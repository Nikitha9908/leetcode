class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[-1])

# Example usage
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))  # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
