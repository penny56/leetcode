class Solution(object):
    def convert(self, s, numRows):
      """
      :type s: str
      :type numRows: int
      :rtype: str
      """
      res = []
      rows = []

      if numRows == 1: return s

      for i in range(numRows):
            rows.append([])

      cycle = 2 * numRows - 2    # 当 numRows = 4 (0,1,2,3) 时，cycle=6 (0,1,2,3,2,1)
      for i in range(len(s)):    # i =     0 1 2 3 4 5 6 7 8 9
            k = i%cycle          # k =     0 1 2 3 4 5 0 1 2 3
            if k < numRows:
                  index = k      # index = 0 1 2 3 2 1 0 1 2 3 
            else:
                  index = cycle-k
            rows[index].append(s[i])

      for i in range(numRows):
            for j in range(len(rows[i])):
                  res.append(rows[i][j])
      return "".join(res)


sol = Solution()
print(sol.convert(s = "PAYPALISHIRING", numRows = 3))