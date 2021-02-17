#-- coding:utf8 --

'''
Created on Feb 16, 2021

1. list排序，
   l = [2,3,5,4]
   l = sorted(l)
   >> l == [2,3,4,5]

@author: mayijie
'''
from __builtin__ import True

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                for z in nums[i+j+1+1:]:
                    if y+z == -x:
                        # verify the existing arrays
                        exist = False
                        for ex in res:
                            if ex == [x, y, z]:
                                exist = True
                                break
                        if not exist:
                            res.append([x, y, z])
        return res

if __name__ == "__main__":
    sol = Solution()
    res = sol.threeSum([-9,14,-7,-8,9,1,-10,-8,13,12,6,9,3,-3,-15,-15,1,8,-7,-4,-6,8,2,-10,8,11,-15,3,0,-11,-1,-1,10,0,6,5,-14,3,12,-15,-7,-5,9,11,-1,1,3,-15,-5,11,-12,-4,-4,-2,-6,-10,-6,-6,0,2,-9,14,-14,-14,-9,-1,-2,-7,-12,-13,-15,-4,-3,1,14,3,-12,3,3,-10,-9,-1,-7,3,12,-6,0,13,4,-15,0,2,6,1,3,13,8,-13,13,11,11,13,14,-6])
    print res