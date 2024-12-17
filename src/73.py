class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        reomveRows = set()
        removeColumns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    reomveRows.add(i)
                    removeColumns.add(j)
        
        print(f"rows = {reomveRows}, columns = {removeColumns}")

        for removeRow in reomveRows:
            matrix[removeRow] = [0] * len(matrix[removeRow])
        for removeColumn in removeColumns:
            for row in matrix:
                row[removeColumn] = 0


        

sol = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]

sol.setZeroes(matrix)

print (f"res = {matrix}")



