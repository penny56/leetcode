#-- coding:utf8 --

'''
Created on Jan 24, 2021

1.

@author: mayijie
'''

class Solution(object):
    
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        j = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == val:
                while j > i:
                    if nums[j] != val:
                        nums[i] = nums[j]
                        j = j - 1
                        break
                    else:
                        j = j - 1
            if i == j:
                if nums[i] == val:
                    return i
                else:
                    return i+1
        

if __name__ == "__main__":
    
    sol = Solution()
    res = sol.removeElement([0,1,2,2,3,0,4,2], 2)
    print (res)