class Solution(object):
    def is_all_same(self, matrix, target_value):
        return set(element for row in matrix for element in row) == {target_value}
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # direct = {'right', 'down', 'left', 'up'}
        direct = 'right'
        i, j = 0, 0

        s = []

        while True:
            if matrix[i][j] != 101:
                s.append(matrix[i][j])
                matrix[i][j] = 101
            if self.is_all_same(matrix, 101):
                return s
            if direct == 'right':
                if i < len(matrix) and matrix[i+1][j] != 101:
                    i += 1
                else:
                    j += 1
                    direct = 'down'
            elif direct == 'down' and matrix[i][j+1] != 101:
                if j < len(matrix[0]):
                    j += 1
                else:
                    i -= 1
                    direct = 'left'
            elif direct == 'left':
                if i > 0 and matrix[i-1][j] != 101:
                    i -= 1
                else:
                    i += 1
                    direct = 'up'
                
                    


        return res


sol = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]

res = sol.spiralOrder(matrix)
print ("res = ", res)





