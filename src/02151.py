#-- coding:utf8 --

'''
Created on Feb 10, 2021

1. list的pop()，是弹出index最大的一个元素
   array = [1,2,3]
   array.pop()    // == 3
   如果要弹出index最小的元素
   array.pop(0)    // == 1
2. list的反转：list.reverse()
3. 在list末尾追加另一个list中的元素
   -- list.extend(list2)
   // a = [1,2,3], b = [4,5,6] 则a.extend(b) : [1,2,3,4,5,6]
   -- list.append(list2)        // 在列表末尾添加新元素
   // a = [1,2,3], b = [4,5,6] 则a.append(b) : [1, 2, 3, [4, 5, 6]]

@author: mayijie
'''

class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        dic = {}
        ls = list(s)
        for i in range(numRows):
            dic[i] = []
        j, flag = 0, -1
        for i in range(len(ls)):
            dic[j].append(ls[i])
            if j == 0 or j == numRows-1:
                flag = -flag
            j += flag
        
        res = []
        for i in range(numRows):
            res.extend(dic[i])
        return ''.join(res)
            

if __name__ == "__main__":
    sol = Solution()
    res = sol.convert("AB", 1)
    print res