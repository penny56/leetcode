class Solution(object):
    '''
    抄袭3指针解法
    '''
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = -10000
        for i, num in enumerate(nums):
            left = i+1
            right = len(nums)-1
            while left < right:
                curr = num+nums[left]+nums[right]
                if curr == target: return target

                if abs(res-target) > abs(curr-target): res = curr

                if curr < target: left += 1
                if curr > target: right -= 1

        return res

sol = Solution()


print(sol.threeSumClosest(nums = [0,0,0], target = 10000))