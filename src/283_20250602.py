class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] == 0:
                    (nums[j], nums[j+1]) = (nums[j+1], nums[j])
            
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums)