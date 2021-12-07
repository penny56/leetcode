#-- coding:utf8 --

'''
Created on Feb 04, 2021

1. 如果要return一个数组，可以直接
   return [i, j] 
2. 切片，在数组的后面加 [:]，如 [0:3] -> 第0，1，2个元素（前3个元素）
   - 如果第一个索引是0，可省略    [:3] -> 就是[0:3]，就是前3个元素
   - [-1]表示倒数第一个元素，则   [-2:] -> 倒数第2个元素和倒数第1个元素，就是[1,2]或[-2,-1]，就是最后俩元素
   - L = range(100)
   - L[:10]    -> 前10个数：[0,1,...,9]
   - L[-10:]   -> 后10个数：[90,91,...,99]
   - L[10:20]  -> 前11~20个数：[10,11,...,19]
   - L[:10:2]  -> 前10个数，每2个取一个：[0,2,4,6,8]
   - L[::5]    -> 所有元素，每5个取一个：[0,5,10,...,95]
   - L[:]      -> 原样复制
   - tuple也可以用：(0,1,2,3,4)[:3]  ->  (0,1,2)
   - string也可以用：'abcde'[:3]  ->  'abc'    比字符串截取简单多了

@author: mayijie
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(len(nums))[i:]:
                if i != j and nums[i] + nums[j] == target:
                    return [i, j] 

if __name__ == "__main__":
    sol = Solution()
    res = sol.twoSum([2,7,11,15], 9)
    print (res)