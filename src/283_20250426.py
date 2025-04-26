class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        curr = 0
        for ahead in range(len(nums)):
            if nums[ahead] == 0:
                # curr stop this time
                pass
            else:
                nums[curr] = nums[ahead]
                curr += 1
        
        for i in range(curr, len(nums)):
            nums[i] = 0
            
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums)