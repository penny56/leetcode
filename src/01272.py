#-- coding:utf8 --

'''
Created on Jan 27, 2021

1. 整型转整型数组，整型数组转整型

@author: mayijie
'''

class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        len1 = len(digits)
        num = 0
        for i in range(len(digits)):
            num = num*10+digits[i]
        res = num+1
        i = 0
        res2= []
        while True:
            res2.append(res%10)
            res = res/10
            i += 1
            if res == 0:
                break
        res3 = res2[::-1]
        len2 = len(res3)
        for i in range(len1-len2):
            res3.insert(0, 0)
        return res3

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.plusOne([0,0,0])
    print res