#-- coding:utf8 --

'''
Created on Jan 21, 2021

1. 通过abs(x)把负数变为正数
2. 删除list中一个元素：
   - 通过index: xs.pop(0)
   - 通过元素自身，如果有多个重复，则先删index靠前的元素：xs.remove(value)
3. 2的3次幂：2**3
4. range()的用法：输入是一个int型参数，输出是一个list，如
   >>> range(10)
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

@author: mayijie
'''

class Solution(object):
    
    # only for x > 0
    def inttoarrayandrev(self, x):
        xs = []
        while x >= 10:
            xs.append(x%10)
            x = x / 10
        xs.append(x)
        return xs
    
    def arraytoint(self, xs):
        x = 0
        while len(xs) > 1:
            x = xs.pop(0) * 10 + x * 10
        x = xs.pop(0) + x
        return x
            
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
        if x > 0:
            xs = self.inttoarrayandrev(x)
            while xs[0] == 0:
                xs.pop(0)
            x = self.arraytoint(xs)
            if x > 2**31 - 1:
                return 0
            return x
        if x < 0:
            xs = self.inttoarrayandrev(abs(x))
            while xs[0] == 0:
                xs.pop(0)
            x = 0 - self.arraytoint(xs)
            if x < -2**31:
                return 0
            return x


if __name__ == "__main__":
    sol = Solution()
    res = sol.reverse(1534236469)
    print res