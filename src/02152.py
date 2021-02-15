#-- coding:utf8 --

'''
Created on Feb 10, 2021

1. 合规的字符串转整型：int(str)
   int("234")        // 234

@author: mayijie
'''
from ctypes.test.test_prototypes import positive_address

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        max, min, i = 2**31-1, -2**31, 0
        positive = True
        temp = list(s)

        while i < len(temp):
            if temp[i] == ' ':
                i += 1
            else:
                temp = temp[i:]
                break
        if temp[0] == '-':
            positive = False
            temp.pop(0)
        elif temp[0] == '+':
            temp.pop(0)
        temp2 = []
        for i in temp:
            if i in ('0','1','2','3','4','5','6','7','8','9'):
                temp2.append(i)
            else:
                break
        if len(temp2) == 0: return 0
        i = int(''.join(temp2))
        if positive:
            if i <= max:
                return i
            else:
                return max
        else:
            if i >= 2**31:
                return min
            else:
                return 0-i
                

if __name__ == "__main__":
    sol = Solution()
    res = sol.myAtoi("+1")
    print res