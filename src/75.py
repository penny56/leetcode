class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # 把2全部移到队尾
        i = 0
        while i != len(nums):
            if nums[i] == 2 and len(nums[i:]) != 0 and set(nums[i:]) != {2}:
                for j in range(i+1, len(nums)):
                    nums[j-1] = nums[j]
                nums[len(nums)-1] = 2
            else:
                i += 1

        # 把0全部移到队头
        i = len(nums)-1
        while i >= 0:
            if nums[i] == 0 and len(nums[:i]) != 0 and set(nums[:i]) != {0}:
                for j in range(i, 0, -1):
                    nums[j] = nums[j-1]
                nums[0] = 0
            else:
                i -= 1



sol = Solution()

nums = [2,1]


sol.sortColors(nums)

print (nums)



