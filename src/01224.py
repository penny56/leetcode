#-- coding:utf8 --

'''
Created on Jan 22, 2021

1. 逻辑运算符优先级：从左到右： if a and b: 先计算a，再计算b。
2. 列表操作：
   --加元素（从尾巴）：list.append(a)
   --删元素（从尾巴）：list.pop()

@author: mayijie
'''

class Solution(object):
    

    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftright = {'(': True, '[': True, '{': True, ')': False, ']': False, '}': False}
        pair = {'(': ')', '[': ']', '{': '}', ')': '(', ']': '[', '}': '{'}
        ls = list(s)
        stack = []
        
        for c in ls:
            if leftright[c]:
                stack.append(c)
            elif len(stack) == 0 or c != pair[stack.pop()]:
                return False
        
        if len(stack) != 0:
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    res = sol.isValid("}")
    print res