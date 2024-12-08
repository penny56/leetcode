class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        res = True

        cell0 = set()
        cell1 = set()
        cell2 = set()

        for i in range(9):
            rows = set()
            columns = set()

            if i%3 == 0:
                cell0.clear()
                cell1.clear()
                cell2.clear()


            for j in range(9):
                if board[i][j] != '.':
                
                    # for rows
                    if board[i][j] in rows:
                        return False
                    else:
                        rows.add(board[i][j])

                    # for columns
                    if board[j][i] in columns:
                        return False
                    else:
                        columns.add(board[j][i])
        
                    # for 9 cells
                    if j//3 == 0:
                        if board[i][j] in cell0:
                            return False
                        else:
                            cell0.add(board[i][j])
                    if j//3 == 1:
                        if board[i][j] in cell1:
                            return False
                        else:
                            cell1.add(board[i][j])
                    if j//3 == 2:
                        if board[i][j] in cell2:
                            return False
                        else:
                            cell2.add(board[i][j])     

        return res
    



sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

res = sol.isValidSudoku(board)
print ("res = ", res)





