class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        if n%2 == 1: return False
        return self.isPowerOfTwo(n//2)
    
sol = Solution()


print(sol.isPowerOfTwo(16))