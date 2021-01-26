#-- coding:utf8 --

'''
Created on Jan 25, 2021

1. 整型转为字符数组：
    >>> i = 123
    >>> str(i)
    '123'
    >>> list(str(i))
    ['1', '2', '3']

@author: mayijie
'''

class Solution(object):
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        target = "1"
        
        if n == 1:
            return target

        tars = list(target)
        i = 2
        while i <= n:
            cnt = 1
            tmp = []
            for j in range(len(tars)):
                ank = tars[j]
                if j < len(tars)-1 and tars[j+1] == ank:
                    cnt = cnt + 1
                else:
                    tmp.append(str(cnt))
                    tmp.append(ank)
                    cnt = 1
            tars = tmp
            i = i + 1

        return ''.join(tars)
                    
                
            
            
        
            

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.countAndSay(3)
    print res