class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1: return nums[0]
        (sumNum, maxSum) = (0, -float('inf'))
        for i in range(len(nums)-k+1):
            if i == 0:
                sumNum = sum(nums[i:i+k])
            else:
                sumNum -= nums[i-1]
                sumNum += nums[i+k-1]
            if sumNum > maxSum: maxSum = sumNum
        
        return maxSum/k
