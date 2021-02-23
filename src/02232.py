#-- coding:utf8 --

'''
Created on Feb 23, 2021

1. 切片array[x:y:z]，其中 x: 起始位置；y: 终止位置（不含）；z: 步长（默认为1）
   array[-1::-1]或者array[::-1]为倒序（逆序）
2. 便利数组同时得到元素和index：
   for i,x in enumerate(array):
     # i就是index，x就是元素
3. for i,x in enumerate(array[a:b])，如果把数组切片用于for循环，并使用index时要小心
   这里的index只是切片后的index，不是数组array的index，如果要得到array的index需要转换。

@author: mayijie
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == nums[0]:
            return 0
        elif target < nums[0]:
            for i,curr in enumerate(nums[::-1]):
                if target > curr:
                    return -1
                elif target == curr:
                    return len(nums)-i-1
        else:
            for i,curr in enumerate(nums[1:]):
                if target < curr:
                    return -1
                elif target == curr:
                    return i+1
        return -1
        
                
            

if __name__ == "__main__":
    sol = Solution()
    res = sol.search([3,1], 3)
    print res