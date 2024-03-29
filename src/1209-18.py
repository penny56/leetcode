'''
Created on Dec 9, 2021

1. 蠢办法
2. if写一行
   1) 正确的格式是：var = val1 if cond else val2，看下面的例子
      a = 2 if x == 1 else a = 7  // wrong
      a = 2 if x == 1 else 7      // correct
   2) 如果只有if，没有else：if cond: var = val1，
      if x == 1: a = 2

@author: mayijie
'''

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        for i, vi in enumerate(nums):
            for j, vj in enumerate(nums):
                if j <= i: continue
                for k, vk in enumerate(nums):
                    if k <= j: continue
                    for l, vl in enumerate(nums):
                        if l <= k: continue
                        if vi+vj+vk+vl == target:
                            sorted = [vi, vj, vk, vl]
                            # 去重
                            sorted.sort()
                            if not sorted in res:
                                res.append(sorted)
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.fourSum([-483,-476,-475,-460,-450,-431,-428,-419,-410,-374,-347,-345,-311,-303,-299,-286,-278,-271,-260,-257,-240,-227,-217,-203,-196,-191,-189,-179,-171,-151,-150,-144,-134,-130,-112,-107,-97,-96,-94,-70,-62,-54,-38,-38,-23,-12,-11,-2,2,4,30,33,38,51,51,54,69,90,108,111,112,112,121,129,163,182,184,194,198,199,210,228,229,232,236,237,249,249,259,282,303,312,317,329,329,342,349,368,375,380,384,393,420,433,441,446,460,474,497], -2306)
    print (res)