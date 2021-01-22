#-- coding:utf8 --

'''
Created on Jan 22, 2021

1. Hash的定义：rom = {'I': 1, 'V': 5}, 是以','为间隔， 不是';'哦。
2. 字符串转列表：
   -- 如果有明显分隔符，如逗号：str.split(',')
   -- 如果是每个字母一个列表元素：list(str)
      >>> list("asdf")
      ['a', 's', 'd', 'f']

@author: mayijie
'''

class Solution(object):
    
    rom = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        rl = list(s)
        i = 0
        
        while len(rl) > 1:
            c1 = rl.pop(0)
            c2 = rl[0]
            if self.rom[c1] >= self.rom[c2]:
                i = i + self.rom[c1]
            else:
                if c1 == 'I' and c2 == 'V':
                    i = i + 4
                    rl.pop(0)
                elif c1 == 'I' and c2 == 'X':
                    i = i + 9
                    rl.pop(0)
                elif c1 == 'X' and c2 == 'L':
                    i = i + 40
                    rl.pop(0)
                elif c1 == 'X' and c2 == 'C':
                    i = i + 90
                    rl.pop(0)
                elif c1 == 'C' and c2 == 'D':
                    i = i + 400
                    rl.pop(0)
                elif c1 == 'C' and c2 == 'M':
                    i = i + 900
                    rl.pop(0)
                else:
                    print "Oops~"
                
        if len(rl) == 1:
            i = i + self.rom[rl.pop(0)]
        
        return i
            
if __name__ == "__main__":
    sol = Solution()
    res = sol.romanToInt("MCMXCIV")
    print res