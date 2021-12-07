#-- coding:utf8 --

'''
Created on Feb 04, 2021

1. 如果要求i与j的和，可以通过在已检索的结果（放在字典里）找target - i，就是j啊。

@author: mayijie
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in dic.keys():
                return [dic[target-nums[i]], i]
            dic[nums[i]] = i
             

if __name__ == "__main__":
    sol = Solution()
    res = sol.twoSum([2,7,11,15], 9)
    print (res)