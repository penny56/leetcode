#-- coding:utf8 --

'''
Created on Feb 23, 2021

1. 超时，需要使用位运算

@author: mayijie
'''

class Solution(object):

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative, times, sum = False, 0, abs(divisor)
        if abs(dividend) < abs(divisor):
            return 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            negative = True
        while sum <= abs(dividend):
            times += 1
            sum += abs(divisor)
        res = 0-times if negative else times
        if res < -2**31 or res > 2**31-1:
            return 2**31-1
        else:
            return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.divide(-2147483648, -2)
    print res