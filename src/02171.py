#-- coding:utf8 --

'''
Created on Feb 17, 2021

1. 递归

@author: mayijie
'''

class Solution(object):

    dic = {'2': ['a','b','c'],
           '3': ['d','e','f'],
           '4': ['g','h','i'],
           '5': ['j','k','l'],
           '6': ['m','n','o'],
           '7': ['p','q','r','s'],
           '8': ['t','u','v'],
           '9': ['w','x','y','z']
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.dic[digits[0]]
        
        current = self.dic[digits[0]]
        later = self.letterCombinations(digits[1:])
        temp = []
        for x in current:
            for y in later:
                temp.append(x+y)
        return temp
        
        
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.letterCombinations("45")
    print (res)