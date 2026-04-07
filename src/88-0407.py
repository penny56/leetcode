class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # screen from the biggest (tail) smaller (left side)
        t1 = m-1
        t2 = n-1
        
        for i in range(len(nums1)-1, -1, -1):
            if t2 >= 0:
                if (nums1[t1] <= nums2[t2]):
                    nums1[i] = nums2[t2]
                    t2 -= 1
                else:
                    nums1[i] = nums1[t1]
                    t1 -= 1
        
        while t2 >= 0:
            nums1[t2] = nums2[t2]
            t2 -= 1
            
        


            
