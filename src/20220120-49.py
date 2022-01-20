'''
Created on Jan 20, 2022

1. 参考答案，比较之前先排序是比较的一种相对好的手段。

@author: mayijie
'''
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        strsSort = strs[:]
        for strSort in enumerate(strsSort):
            ll = list(strSort[1])
            ll.sort()
            strSorted = "".join(ll)
            strsSort[strSort[0]] = strSorted

        for strSortOut in strsSort:
            if strSortOut != "":
                temp = []
                for strSortIn in enumerate(strsSort):
                    if strSortOut == strSortIn[1]:
                        temp.append(strs[strSortIn[0]])
                        strs[strSortIn[0]] = ""
                        strsSort[strSortIn[0]] = ""
                res.append(temp)
        return [[""]] if res == [] else res

if __name__ == "__main__":
    sol = Solution()
    res = sol.groupAnagrams([""])
    print (res)