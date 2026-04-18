class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        (leftSum, rightSum) = (0, sum(nums[1:]))
        for i, axis in enumerate(nums):
            if i != 0:
                leftSum += nums[i-1]
                rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            
        return -1
