class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        windows_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            # add the right boundary to window sum
            windows_sum += nums[right]

            # judge exceed the target?
            while windows_sum >= target:
                # record the new min_length
                min_length = min(min_length, right-left+1)

                # try move left side to right
                windows_sum -= nums[left]
                left += 1
            

        if min_length != float('inf'):
            return min_length
        else:
            return 0
