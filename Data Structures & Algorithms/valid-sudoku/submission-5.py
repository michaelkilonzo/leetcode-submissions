class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subsquares = [set() for _ in range(9)]
        
        for row_idx in range(9):
            for col_idx in range(9):
                subsquare_idx = ((row_idx // 3) * 3 + (col_idx // 3))
                if board[row_idx][col_idx] != ".":
                    # validate rows and cols and subsquare
                    if board[row_idx][col_idx] in rows[row_idx] or board[row_idx][col_idx] in cols[col_idx] or board[row_idx][col_idx] in subsquares[subsquare_idx]:
                        return False
                    # add number to row and col sets 
                    rows[row_idx].add(board[row_idx][col_idx])
                    cols[col_idx].add(board[row_idx][col_idx])
                    # add number subsquares set
                    subsquares[subsquare_idx].add(board[row_idx][col_idx])

        return True


