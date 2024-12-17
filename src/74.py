class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for i in range(len(matrix)-1, -1, -1):
            if matrix[i][0] <= target and target <= matrix[i][-1]:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target: return True
        return False
    

        


        

sol = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

res = sol.searchMatrix(matrix, target)

print (res)



