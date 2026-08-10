class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subsquares = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                row_idx = i
                col_idx = j
                subsquare_idx = ((row_idx // 3) * 3 + (j // 3))
                if board[i][j] != ".":
                    # validate rows and cols and subsquare
                    if board[row_idx][col_idx] in rows[row_idx] or board[row_idx][col_idx] in cols[col_idx] or board[row_idx][col_idx] in subsquares[subsquare_idx]:
                        return False
                    # add number to row and col sets 
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    # add number subsquares set
                    subsquares[subsquare_idx].add(board[row_idx][col_idx])

        return True


