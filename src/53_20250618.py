class Solution(object):
    def maxSubArray(self, nums):
        i = 0
        current_sum = max_sum = nums[0]

        while i < len(nums) - 1:
            i += 1
            # 要么接着之前的和，要么从当前数重新开始
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))