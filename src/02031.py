#-- coding:utf8 --

'''
Created on Jan 27, 2021

1. Python要交换两个变量，不用3个表达式：
   x, y = y, x
2. if else可以写在一行，但是如果只有if，没有else是不行的，就直接写两行吧。
   x=a if a>b else b 可以，x=a if a>b 不行

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
    print res