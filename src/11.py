class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxBlue, maxi, maxj = 0, 0, 0
        for i, hi in enumerate(height):
            for j, hj in enumerate(height):
                if j > i:
                    blue = (j-i)*min(hi, hj)
                    if blue > maxBlue:                        
                        maxBlue, maxi, maxj = max(maxBlue, blue), max(maxi, i), max(maxi, j)
        
        print (f"maxBlue = {maxBlue}, maxi = {maxi}, maxj = {maxj}")

                


sol = Solution()

res = sol.maxArea([1,8,6,2,5,4,8,3,7])
print ("res = ", res)