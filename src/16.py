class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        resList = []
        j = len(nums) - 1
        for i in range(len(nums)):
            if i == j: break
            while nums[i]+nums[j] > target and j > i:
                j -= 1
            if nums[i]+nums[j] == target and j != i:
                resList.append([nums[i], nums[j]])
        return resList
        
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        resSet = set()
        for i, a in enumerate(nums):
            tmp = nums[:]
            tmp.pop(i)
            print (f"i = {i}, a = {a}")
            twoList = self.twoSum(tmp, -a)
            if twoList != None:
                for two in twoList:
                    three = two[:]
                    three.append(a)
                    three.sort()
                    resSet.add(tuple(three))
                    print (f"three: {tuple(three)}")
        
        resArray = []
        for a in resSet:
            resArray.append(list(a))

        return resArray


# nums = [2,7,11,15]
target = 1
nums = [-1,2,1,-4]


sol = Solution()

res = sol.threeSumClosest(nums, target)
print ("res = ", res)