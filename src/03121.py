#-- coding:utf8 --

'''
Created on Mar 12, 2021

1. <抄作业>知道：爬到n级台阶的方案，是爬到第n-1级台阶的方案（再爬1级）与第n-2级台阶的方案（再爬2级）之和。 ==> 递推公式 F(n) = F(n-1) + F(n-2) ==> 递归
   斐波那契数列

@author: mayijie
'''

class Solution(object):
    
    dic = {}
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        if (n == 1):
            return 1
        if (n == 2):
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        '''
        pre1, pre2 = 1, 2
        if n == 1:
            return pre1
        if n == 2:
            return pre2
        while n>2:
            curr = pre1 + pre2
            pre1 = pre2
            pre2 = curr
            n -= 1
        return curr
        

if __name__ == "__main__":
    sol = Solution()
    res = sol.climbStairs(5)
    print res