class Solution:
    def totalNQueens(self, n):
        def backtrack(row, columns, diag1, diag2):
            # If we have placed queens in all rows, we've found a valid solution
            if row == n:
                return 1
            count = 0
            for col in range(n):
                # Check if column or diagonals are under attack
                if col in columns or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # Mark the current column and diagonals as occupied
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                # Recurse to place queens in the next row
                count += backtrack(row + 1, columns, diag1, diag2)
                # Backtrack by removing the queen and unmarking the column and diagonals
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
            return count

        # Sets to track attacked columns and diagonals
        columns = set()
        diag1 = set()
        diag2 = set()
        
        return backtrack(0, columns, diag1, diag2)

# Test example
param_1 = 4
sol = Solution()
print(sol.totalNQueens(param_1))  # Output: 2
