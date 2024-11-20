class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                print (f"index = {i} {j}")
                print (f"        {a} {b}")
                if i != j and a + b == target:
                    return [i, j]        

nums = [2,7,11,15]
target = 9

sol = Solution()

res = sol.twoSum(nums, target)
print ("res = ", res)