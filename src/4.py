class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalCnt = len(nums1)+len(nums2)
        even = True
        if totalCnt == 0: return 0

        if len(nums1)+len(nums2) == 1:
            if len(nums1) == 1: return float(nums1[0])
            if len(nums2) == 1: return float(nums2[0])
             
        while len(nums1)+len(nums2) > 2:
            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[0] <= nums2[0]:
                    nums1.pop(0)
                else:
                    nums2.pop(0)
                even = False
            else:
                break
            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[-1] >= nums2[-1]:
                    nums1.pop(-1)
                else:
                    nums2.pop(-1)
                even = True
            else:
                break
        
        if not even:
            if len(nums1) > 0:
                nums1.pop(-1)
            else:
                nums2.pop(-1)

        while len(nums1) > 2:
            nums1.pop(0)
            nums1.pop(-1)

        while len(nums2) > 2:
            nums2.pop(0)
            nums2.pop(-1)
               
        if len(nums1) == 2:
            return (nums1[0]+nums1[1])/2
        if len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0]+nums2[0])/2
        if len(nums1) == 1 and len(nums2) == 0:
            return float(nums1[0])
        if len(nums1) == 0 and len(nums2) == 1:
            return float(nums2[0])
        if len(nums2) == 2:
            return (nums2[0]+nums2[1])/2
        



sol = Solution()

nums1 = [2,2,4,4]
nums2 = [2,2,2,4,4]

res = sol.findMedianSortedArrays(nums1, nums2)
print ("res = ", res)





