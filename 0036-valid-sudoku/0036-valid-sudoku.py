class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] != '.':
                    s.add(board[i][j])
        #col
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i] != '.':
                    s.add(board[j][i])      
        #boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                s = set()
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] in s:
                            return False
                        elif board[i+m][j+n] != '.':
                            s.add(board[i+m][j+n])
                            
        return True