from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return nums1
        if n == 0: return nums1
        # nums1 与 nums2 都从尾向头部遍历，这样就可以不会覆盖还没有使用的元素

        (i, j, k) = (m-1, n-1, m+n-1)

        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        
        if i < 0:
            nums1[:k+1] = nums2[:j+1]
        
        print(f'{nums1}')
        return None


if __name__ == '__main__':
    sol = Solution()
    sol.merge([2, 0], 1, [1], 1)
    

