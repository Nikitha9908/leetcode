class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # DP table, dp[i][j] will be True if s[0..i-1] matches p[0..j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Initialize the first row (empty string s matches pattern p with stars)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]  # Match any single character
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # Match zero or more characters
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]  # Exact character match
        
        # The result is in the bottom-right cell of the DP table
        return dp[m][n]

# Example test cases
sol = Solution()
print(sol.isMatch("aa", "a"))  # Output: False
print(sol.isMatch("aa", "*"))  # Output: True
print(sol.isMatch("cb", "?a"))  # Output: False
