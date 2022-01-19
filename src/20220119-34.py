'''
Created on Jan 19, 2022

1. 

@author: mayijie
'''
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        for curr in enumerate(nums):
            if curr[1] < target:
                continue
            elif curr[1] == target:
                if res[0] == -1:
                    (res[0], res[1]) = (curr[0], curr[0])
                else:
                    res[1] = curr[0]
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.searchRange([], 6)
    print (res)