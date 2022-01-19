'''
Created on Jan 19, 2022

1. List的遍历：
   1) 只取list中的元素，输出：2  3  4
      nums = [2,3,4]
      for curr in nums:
          print (curr)
   2) 取list中的元素和index，输出：(0,2)  (1,3)  (2,4)
      nums = [2,3,4]
      for curr in enumerate(nums):
          print (curr)
      可以看到输出是Tuple，第一个元素是元素index，第二个元素是元素本身，所以可以用curr[0]和curr[1]来表示
          print (curr[0], curr[1])

@author: mayijie
'''
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        for curr in enumerate(nums):
            if curr[1] == target:
                if res[0] == -1:
                    (res[0], res[1]) = (curr[0], curr[0])
                else:
                    res[1] = curr[0]
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.searchRange([], 6)
    print (res)