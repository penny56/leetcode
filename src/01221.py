#-- coding:utf8 --

'''
Created on Jan 22, 2021



@author: mayijie
'''

class Solution(object):
    
    # only for x > 0
    def inttoarrayandrev(self, x):
        xs = []
        while x >= 10:
            xs.append(x%10)
            x = x / 10
        xs.append(x)
        return xs
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x > 0:
            xs = self.inttoarrayandrev(x)
            while len(xs)/2 > 0:
                i = xs.pop(0)
                j = xs.pop(len(xs) - 1)
                if i != j:
                    return False
            return True
        else:
            return False

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.isPalindrome(0)
    print res