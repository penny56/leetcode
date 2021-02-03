#-- coding:utf8 --

'''
Created on Jan 27, 2021

1. 

@author: mayijie
'''

class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        cnt = m+n
        while True:
            if m-1 >= 0 and n-1 >= 0:
                if nums1[m-1] >= nums2[n-1]:
                    nums1[m+n-1] = nums1[m-1]
                    m -= 1
                else:
                    nums1[m+n-1] = nums2[n-1]
                    n -= 1
            else:
                break
        if n == 0:
            pass 
        else:
            for j in range(n):
                nums1[j] = nums2[j]
        for i in range(cnt):
            print nums1[i] 
        return

if __name__ == "__main__":
    sol = Solution()
    sol.merge([0], 0, [1], 1)