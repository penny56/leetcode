#-- coding:utf8 --

'''
Created on Jan 21, 2021

1. Python要定义类，main开头要加 if __name__ == "__main__":，并且定义类对象
2. 把功能放进方法里，通过 sol.twoSum()来调用，参数可以构造函数里赋值，也可以这里赋值
3. 类方法的第一个参数是self，调用类函数也需要用self.method()
4. list的用法：初始化是 x = [], 加元素的方法是 x.append(y)
5. 注意人要的是index，sort之后index会变，如果只有一种可能，说明数组中任意两个元素值都不同，用hash吧。
6. dict的用法：初始化是 d = {}，遍历：for key, value in dic.items():

@author: mayijie
'''

class Solution(object):

    def bubble_sort(self, nums):
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        dic = {}
        
        # make the dict key = the array index, value = array element
        j = 0
        for i in nums:
            dic[j] = i
            j = j + 1
            
        nums = self.bubble_sort(nums)

        x = 0
        y = len(nums) - 1

        while x < y:
            temp = nums[x] + nums[y]
            if temp == target:
                '''
                res.append(dic[nums[x]])
                res.append(dic[nums[y]])
                '''
                for key, value in dic.items():
                    if value == nums[x] or value == nums[y]:
                        res.append(key)
                return res
            if temp < target:
                x = x + 1
            if temp > target:
                y = y - 1
        return None

if __name__ == "__main__":
    sol = Solution()
    res = sol.twoSum([3,3], 6)
    
    print res
    