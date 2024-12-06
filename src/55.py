class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        i 相当于一个小人，小人每个循环都会向前走一格，不会停。
        k 相当于一直向前铺路，每个循环会根据当前可以向前铺的最长的路铺路。
        如果小人走到了没有铺的路上，就返回False
        如果小人走到了路的尽头，就返回True
        '''
        k = 0
        for i in range(len(nums)):
            if i > k: return False
            k = max(k, i+nums[i])

        return True


sol = Solution()

res = sol.canJump([3,2,1,0,4])
print ("res = ", res)





