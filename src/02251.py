#-- coding:utf8 --

'''
Created on Feb 25, 2021

1. 抄解法，思路：找两个变量，
                    -- 最大收益
                    -- 最小价格
   每次loop都会更新这两个变量，最大收益 = （当前价格 - 最小价格）与最大收益对比，取最大
                           最小价格 = 当前价格与最小价格对比，最最小
   最终返回“最大收益”。

@author: mayijie
'''

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxprofit, minprice = 0, 10**5
        for price in prices:
            maxprofit = max(price-minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

if __name__ == "__main__":
    sol = Solution()
    res = sol.maxProfit([7,1,5,3,6,4])
    print res