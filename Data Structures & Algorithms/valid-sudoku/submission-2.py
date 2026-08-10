class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subsquares = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # validate rows and cols and subsquare
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in subsquares[((i // 3) * 3 + (j // 3))]:
                        return False
                    # add number to row and col sets 
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    # validate subsquares
                    subsquares[((i // 3) * 3 + (j // 3))].add(board[i][j])

        return True


