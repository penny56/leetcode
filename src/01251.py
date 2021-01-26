#-- coding:utf8 --

'''
Created on Jan 25, 2021

1. 字符串长度和数组长度一样，也是用len(str)
   >>> t = "asdf"
   >>> len(t)
   4
2. 注意，如果haystack剩余没有检查的部分，比needle的全部还在小，就不用再检查了， 这个需要用i == len(haystack) - len(needle)判断一下，
   否则会有一大串的needle，只有最后一个字母与haystack最后一个字母不同，其余都相同的case，会导致超时。

@author: mayijie
'''

class Solution(object):
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i+j < len(haystack) and haystack[i+j] == needle[j]:
                    if j == len(needle) - 1:
                        return i
                else:
                    break
            if i == len(haystack) - 1 or i == len(haystack) - len(needle):
            # 或者这里的判断写为
            # i >= len(haystack) - len(needle)：
                return -1

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.strStr("mississippi", "pi")
    print res
