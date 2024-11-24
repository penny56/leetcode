class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = set()
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i != j and a + b == target:
                    sorted_list = sorted([a, b])
                    res.add(tuple(sorted_list))
        return res
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resSet = set()
        for i, a in enumerate(nums):
            tmp = nums[:]
            tmp.pop(i)
            print (f"i = {i}, a = {a}")
            twoSet = self.twoSum(tmp, -a)
            if twoSet != None:
                for two in twoSet:
                    twoList = list(two)
                    twoList.append(a)
                    twoList.sort()
                    resSet.add(tuple(twoList))
                    print (f"twoSum: {tuple(twoList)}")
        
        resArray = []
        for a in resSet:
            resArray.append(list(a))

        return resArray


# nums = [2,7,11,15]
# target = 9
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]


sol = Solution()

res = sol.threeSum(nums)
print ("res = ", res)