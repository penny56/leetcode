#-- coding:utf8 --

'''
Created on Feb 24, 2021

1. 抄作业：贪心算法：只分3步，用到3个变量
   1. 3个变量：
          当前值
          之前和
          最大各
   2. 3步：
          若之前和小于0，则去掉之前和（之前和变为0）
          更新之前和（之前和=之前和+当前值）
          之前和与最大和比较，若大于最大和，则更新最大和

@author: mayijie
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        presum, maxsum = 0, -10**5
        for i in nums:
            if presum < 0: presum = 0
            presum += i
            if presum > maxsum: maxsum = presum
        return maxsum
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.maxSubArray([-100000])
    print res