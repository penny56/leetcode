class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        (i, j, cnt) = (0,0,1)
        tailIndex = len(nums)-1
        if len(nums) <= 1: return 0

        while i < len(nums):
            (currDist, maxDist) = (0, 0)
            
            for j in range(i+1, i+nums[i]+1):
                # j 从 i+1 开始，到 i+nums[i] 结束
                
                if j == tailIndex: return cnt # 如果到了末尾了，不用再跳了
                
                currDist = nums[j]+(j-i) # currDist不但要算向右跳的距离，还要加上距离左边的i的距离。
                
                if currDist > maxDist:
                    maxDist = currDist
                    maxIndex = j

            # do jump
            cnt += 1
            i = maxIndex
            if i >= tailIndex: return cnt
                
            

sol = Solution()

nums = [1,2,1,1,1]

res = sol.jump(nums)
print ("res = ", res)





