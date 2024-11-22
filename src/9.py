class Solution(object):
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x > 9 and x % 10 == 0:
            return False
        
        later = 0
        while x > later:
            later = later * 10 + x % 10
            x = x // 10
        
        if x == later or x == later // 10:
            return True
        else:
            return False

sol = Solution()

res = sol.isPalindrome(121)
print ("res = ", res)