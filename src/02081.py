#-- coding:utf8 --

'''
Created on Feb 08, 2021

1. 学习leetcode算法

@author: mayijie
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0 or (x >= 10 and x%10 == 0):
            return False
        elif x < 10:
            return True
        else:
            later = 0
            while True:
                later = later*10+x%10
                x = x/10
                if later == x or later == x/10:
                    return True
                elif later > x:
                    return False

if __name__ == "__main__":
    sol = Solution()
    res = sol.isPalindrome(12233221)
    print (res)