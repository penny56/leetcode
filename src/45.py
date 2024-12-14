class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        cnt = 0
        while i < len(nums)-1:
            test = 0
            k = 0
            j = 0
            if nums[i] == 1:
                cnt += 1
                i += 1
                continue

            for j in range(1, nums[i]+1):
                if i + j >= len(nums) - 1:
                    return cnt + 1
                temp = nums[i+j] + j 
                if temp > test:
                    k = j
                    test = temp
            cnt += 1
            i += k 
        return cnt

sol = Solution()

nums = [2,1]


res = sol.jump(nums)
print ("res = ", res)





