class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        res = len(nums)

        while left <= right:
            mid = (left+right)//2
            if target <= nums[mid]:
                right = mid-1
                res = mid
            else:
                left = mid+1

        return res

if __name__ == "__main__":

    sol = Solution()

    res = sol.searchInsert([1,3,5,6], 2)
    print (f"res = {res}")

