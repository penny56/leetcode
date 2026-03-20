class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        if n == 0: return

        # both m and n not equals 0
        nums1copy = nums1[:m]
        # print(f'nums1copy = {nums1copy}')
        i = 0
        while nums1copy and nums2:
            if nums1copy[0] <= nums2[0]:
                nums1[i] = nums1copy[0]
                nums1copy.pop(0)
            else:
                nums1[i] = nums2[0]
                nums2.pop(0)
            i += 1
        
        if nums1copy:
            nums1[i:] = nums1copy[:]
        else:
            nums1[i:] = nums2[:]


        return
