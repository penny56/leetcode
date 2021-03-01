#-- coding:utf8 --

'''
Created on Feb 25, 2021

1. String大小写转换：注意，只对字符串中的字母有效，对空格、数字、标点保留原样。
   STR = str.upper()
   str = STR.lower()

2. 字符也可以用 > < == 来判断，如可以用 (c >= 'a' and c <= 'z') 来判断字符c是不是“小写字母”

@author: mayijie
'''

class Solution(object):
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        lit = s.lower()
        litarr = []
        for c in lit:
            if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9'):
                litarr.append(c)
        while len(litarr) >= 2:
            begin = litarr.pop(0)
            end = litarr.pop()
            if begin != end:
                return False
        return True
            

if __name__ == "__main__":
    sol = Solution()
    res = sol.isPalindrome("0P")
    print res