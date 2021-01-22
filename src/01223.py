#-- coding:utf8 --

'''
Created on Jan 22, 2021

1. 字典操作：清除：dic.clear()；查key/value对的个数：len(dic)
2. 列表转字符串：''.join(str)

@author: mayijie
'''

class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        res = []
        dic= {}
        i = 0
        
        while 1:

            for str in strs:
                lstr = list(str)
                if len(lstr) > i:
                    dic[lstr[i]] = 1
                else:
                    return ''.join(res)
            
            if len(dic) == 1:
                res.append(dic.keys()[0])
                i = i + 1
            else:
                return ''.join(res)
            dic.clear()

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.longestCommonPrefix(["dog","racecar","car"])
    print res