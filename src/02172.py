#-- coding:utf8 --

'''
Created on Feb 17, 2021

1. 没解出来

@author: mayijie
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        prev = []
        nums = sorted(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                for k, z in enumerate(nums[i+1+j+1:]):
                    for w in nums[i+1+j+1+k+1:]:
                        print str(x) + ' ' + str(y) + ' ' + str(z) + ' ' + str(w)
                        if x+y+z+w == target:
                            if prev == []:
                                prev = [x, y, z, w]
                            else:
                                if prev != [x, y, z, w]:
                                    res.append([x, y, z, w])
                                    prev = [x, y, z, w]
        return res
        
if __name__ == "__main__":
    sol = Solution()
    res = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
    print res