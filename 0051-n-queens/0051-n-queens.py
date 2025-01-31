class Solution:
    def solveNQueens(self, n):
        def backtrack(row, cols, diagonals, anti_diagonals, board):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                diag = row - col
                anti_diag = row + col
                
                if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                    continue
                
                # Place the queen
                board[row][col] = 'Q'
                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)
                
                # Move to the next row
                backtrack(row + 1, cols, diagonals, anti_diagonals, board)
                
                # Backtrack: Remove the queen
                board[row][col] = '.'
                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)

        result = []
        board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result

# Example Usage
solution = Solution()
print(solution.solveNQueens(4))  
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solution.solveNQueens(1))  
# Output: [["Q"]]
