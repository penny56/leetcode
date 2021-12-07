#-- coding:utf8 --

'''
Created on Jan 23, 2021



@author: mayijie
'''

class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        anchor = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != anchor:
                anchor = nums[i]
                j = j+1
                nums[j] = anchor
        return j+1

if __name__ == "__main__":
    sol = Solution()
    res = sol.removeDuplicates([])
    print (res)