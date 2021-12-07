#-- coding:utf8 --

'''
Created on Jan 27, 2021

1. 字符串去掉头尾空格：str.strip()
2. 数组反序：array[::-1]

@author: mayijie
'''

class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip()) == 0:
            return 0
        
        arr = s.split(' ')
        rarr = arr[::-1]
        for i in range(len(rarr)):
            if len(rarr[i].strip()) != 0:
                return len(rarr[i].strip())

if __name__ == "__main__":
    sol = Solution()
    res = sol.lengthOfLastWord("Helloq World ")
    print (res)