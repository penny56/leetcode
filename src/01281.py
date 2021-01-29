#-- coding:utf8 --

'''
Created on Jan 27, 2021

1. if,else写在一行，如果是多个表达式，用tuple:
   more, less = (a, b) if len(a) >= len(b) else (b, a)

@author: mayijie
'''

class Solution(object):
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        bjs, js = (a, b) if len(a) >= len(b) else (b, a)
        
        ra = list(bjs)[::-1]
        rb = list(js)[::-1]
        temp = 0
        for i in range(len(ra)):
            if i < len(rb):
                if int(ra[i]) + int(rb[i]) + temp == 3:
                    temp = 1
                elif int(ra[i]) + int(rb[i]) + temp == 2:
                    ra[i] = '0'
                    temp = 1
                elif int(ra[i]) + int(rb[i]) + temp == 1:
                    ra[i] = '1'
                    temp = 0
                else:
                    temp = 0
            else:
                if int(ra[i]) + temp == 2:
                    ra[i] = '0'
                    temp = 1
                elif int(ra[i]) + temp == 1:
                    ra[i] = '1'
                    temp = 0
                else:
                    print "error"
        if temp == 1:
            ra.append('1')
        rra = ra[::-1]
        return ''.join(rra)
                    
                

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.addBinary("11", "1")
    print res