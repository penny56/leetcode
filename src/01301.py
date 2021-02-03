#-- coding:utf8 --

'''
Created on Jan 27, 2021

1. 

@author: mayijie
'''

class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
        
        i = 1
        while True:
            if i**2 == x:
                return i
            elif i**2 < x:
                i += 1
            else:
                return i-1

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.mySqrt(8)
    print res
    