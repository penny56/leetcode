class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]      
        """
        nums.sort()
        j = len(nums) - 1
        for i in range(len(nums)):
            if i == j: break
            while nums[i]+nums[j] > target:
                j -= 1
            if nums[i]+nums[j] == target: return [i, j]



sol = Solution()

res = sol.twoSum([3,2,4], 6)
print ("res = ", res)