'''
Created on Jan 7, 2022

1. 看了题解才会
   1) 如果才能找到下一个最大的序列呢？
      - 找左边的‘较小值’和右边的‘较大值’交换
      - ‘较小值’要尽可以靠右，而‘较大值’要尽可能的小
      - 交换完成后，还要将‘较大值’右侧升序排列
   2) 不动用其它存储空间，如果给一个数列‘升序排列’？
      - 因为其实已知这个序列是降序排列的，只要把这个降序列表依次首尾对调就可以。

@author: mayijie
'''


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums[:]
        tmp.sort(reverse=True)
        if nums == tmp:
            nums.sort()
            print (nums)
            return


        for i in list(range(len(nums)-1,0,-1)):
            if nums[i-1] < nums[i]:
                i = i-1
                print ("left is here: index=", i)
                for j in list(range(len(nums)-1, i, -1)):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        ''' The question requires no more storage space
                        temp = nums[i+1:]
                        temp.sort()
                        nums = nums[:i+1] + temp
                        '''
                        left, right = i + 1, len(nums) - 1
                        while left < right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1
                        print (nums)
                        return

if __name__ == "__main__":
    sol = Solution()
    sol.nextPermutation([1,3,2])
