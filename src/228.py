class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return ["0"]


        flag = False
        stack = []
        left = nums[0]
        right = nums[len(nums)-1]
        for num in range(left, right+2):
            if num == right+1 and flag and len(s) != 0:
                # 专门处理最后一个s
                stack.append(s)
                break
            if num in nums and not flag:
                s = []
                s.append(num)
                flag = True
            elif num in nums and flag:
                s.append(num)
            elif num not in nums and not flag:
                pass
            elif num not in nums and flag:
                stack.append(s)
                flag = False
        
        stackNums = []
        for s in stack:
            if len(s) == 1:
                string = str(s[0])
            else:
                string = str(s[0]) + "->" + str(s[-1])
            stackNums.append(string)
        
        return stackNums


sol = Solution()


print(sol.summaryRanges([-2147483648,0,2,3,4,6,8,9]))