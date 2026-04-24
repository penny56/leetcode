class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0:
            return

        tail1 = m-1
        tail2 = n-1
        for i in range(m+n-1, -1, -1):
            if nums1[tail1] <= nums2[tail2]:
                nums1[i] = nums2[tail2]
                tail2 -= 1
            else:
                nums1[i] = nums1[tail1]
                tail1 -= 1
            
            if tail1 < 0 or tail2 < 0: break
        
        # 如果是tail1 != 1，不用管；如果是tail2 != 0，就需要再移动一下
        while tail2 >= 0:
            nums1[i] = nums2[tail2]
            tail2 -= 1
            i -= 1
        
        return
