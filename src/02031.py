#-- coding:utf8 --

'''
Created on Jan 27, 2021

1. Python要交换两个变量，不用3个表达式：
   x, y = y, x
   -- 同理，两个赋值语句也可以写在一行，如： x, y = 0, 1

@author: mayijie
'''

class Solution(object):

    def bubble_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range (len(nums)-1-i):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        return nums

if __name__ == "__main__":
    sol = Solution()
    res = sol.bubble_sort([3,17,2,8,2,4])
    print (res)