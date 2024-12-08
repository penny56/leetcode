class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        res = True

        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])

        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
        
        s0 = set()
        s1 = set()
        s2 = set()
        
        for i in range(0, 9):
            
            if i == 0 or i == 3 or i == 6:
                s0.clear()
                s1.clear()
                s2.clear()

            for j in range(0, 9):
                if j < 3 and board[i][j] != '.':
                    if board[i][j] in s0:
                        return False
                    else:
                        s0.add(board[i][j])
                if j > 2 and j < 6 and board[i][j] != '.':
                    if board[i][j] in s1:
                        return False
                    else:
                        s1.add(board[i][j])
                if j > 5 and board[i][j] != '.':
                    if board[i][j] in s2:
                        return False
                    else:
                        s2.add(board[i][j])     

        return res
    



sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".", board ="2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

res = sol.isValidSudoku(board)
print ("res = ", res)





