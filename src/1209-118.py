'''
Created on Dec 9, 2021

1. 

@author: mayijie
'''

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        (cnt, cur, res) = (1, list(), list())
        while cnt <= numRows:
            for i in range(1, cnt+1):
                if i == 1: cur = [1]
                elif i == 2: cur = [1, 1]
                else:
                    tmp = [1]
                    for i in range(len(cur)-1):
                        tmp.append(cur[i] + cur[i+1])
                    tmp.append(1)
                    cur = tmp
            res.append(cur)
            cnt += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    res = sol.generate(5)
    print (res)