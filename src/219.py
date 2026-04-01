class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # abs(i-j) <= k 考虑用slice nums[i:i+k+1]

        for i in range(len(nums)):
            temp = nums[i:i+k+1]
            s = set(temp)
            if len(s) != len(temp): return True
        
        return False
