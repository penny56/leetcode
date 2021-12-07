#-- coding:utf8 --

'''
Created on Mar 1, 2021

1. set 操作:
   - 定义：s = set([1,2,3])
   - 加元素：s.add(4)
   - 减元素：s.remove(4)
   - 判断是否存在：if i in s:

@author: mayijie
'''

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set([])
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        for i in s:
            return i
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.singleNumber([4,1,2,1,2])
    print (res)