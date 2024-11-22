class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1: return s

        ls = list(s)
        dict = {}
        j = 0
        dir = -1
        for i in range(len(ls)):
            
            dict[i] = [' '] * numRows
            dict[i][j] = ls[i]
            if j == 0 or j == numRows-1:
                dir = -dir
            j = j+dir

        res = []

        for i in range(numRows):
            for j in range(len(ls)):
                if dict[j][i] != ' ':
                    res.append(dict[j][i])
        
        return "".join(res)

s = "AB"

sol = Solution()

res = sol.convert(s, 1)
print ("res = ", res)