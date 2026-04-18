class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        (r1, r2) = ([], [])
        res = [r1, r2]

        for n1 in nums1:
            if n1 not in nums2 and n1 not in r1: r1.append(n1)
        
        for n2 in nums2:
            if n2 not in nums1 and n2 not in r2: r2.append(n2)
        
        return res
