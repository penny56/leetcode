class Solution(object):
    '''
    抄袭3指针解法
    '''
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        s = set()
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            left = i+1
            right = len(nums)-1
            while left < right:
                if num+nums[left]+nums[right] < 0:
                    left += 1
                elif num+nums[left]+nums[right] == 0:
                    if tuple([num, nums[left], nums[right]]) not in s:
                        s.add(tuple([num, nums[left], nums[right]]))
                        res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                else:
                    right -= 1
        return res

    '''
    对极端情况超时
    '''
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = set()
        res = []
        for i, a in enumerate(nums):
            numsa = nums[:i]+nums[i+1:]
            for j, b in enumerate(numsa):
                numsab = numsa[:j]+numsa[j+1:]
                if 0-(a+b) in numsab:
                    temp = tuple(sorted([a, b, 0 - (a + b)]))
                    if temp not in s:
                        s.add(temp)
                        res.append(list(temp))

        return res

sol = Solution()


print(sol.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))