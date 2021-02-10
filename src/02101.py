#-- coding:utf8 --

'''
Created on Feb 10, 2021

1. 判断数组中是否包含某个元素，若有则返回元素index
   if s in array:
     index = array.index(s)
   else:
     // 不包含，如果不判断有没有直接取index，会raise exception

@author: mayijie
'''
from __builtin__ import True

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tarr = []
        max = 0
        for ls in list(s):
            if ls in tarr:
                tarr = tarr[tarr.index(ls)+1:]
            tarr.append(ls)
            if len(tarr) > max:
                max = len(tarr)
        return max
                

if __name__ == "__main__":
    sol = Solution()
    res = sol.lengthOfLongestSubstring("")
    print res