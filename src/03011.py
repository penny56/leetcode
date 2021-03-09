#-- coding:utf8 --

'''
Created on Mar 1, 2021

1. 删除字典中的某个元素：del dic[i]

@author: mayijie
'''
from __builtin__ import True

class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if dic.has_key(i):
                del dic[i]
            else:
                dic[i] = True
        for i in dic.keys():
            return i
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.singleNumber([4,1,2,1,2])
    print res