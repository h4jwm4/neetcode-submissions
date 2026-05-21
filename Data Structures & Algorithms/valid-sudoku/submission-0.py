class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking duplicates in rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] !=  ".":
                    s.add(board[i][j])
        
        # Checking duplicates in cols
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i] !=  ".":
                    s.add(board[j][i])

        # Checking duplicates in boxes
        for i in range(0,9, 3):
            for j in range(0, 9, 3):
                s = set()
                for l in range(0, 3):
                    for m in range(0,3):
                        if board[i+l][j+m] in s:
                            return False
                        elif "." != board[i+l][j+m]:
                            s.add(board[i+l][j+m])
        return True