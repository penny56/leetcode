#-- coding:utf8 --

'''
Created on Feb 24, 2021

1. 谁说用max(a,b)就不会超时？

@author: mayijie
'''

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi = 0
        for i,x in enumerate(prices[::-1]):
            for j,y in enumerate(prices[(-1-i)::-1]):
                maxi = max(maxi, x-y)
        return maxi

if __name__ == "__main__":
    sol = Solution()
    res = sol.maxProfit([7,1,5,3,6,4])
    print res