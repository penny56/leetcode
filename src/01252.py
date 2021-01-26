#-- coding:utf8 --

'''
Created on Jan 25, 2021

1. 注意边界

@author: mayijie
'''

class Solution(object):
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)):
            if nums[i] >=  target:
                return i
        return len(nums)

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.searchInsert([1,3,5,6], 0)
    print res