class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Record the index and value of nums array
        vIndex = dict()
        for i, v in enumerate(nums):
            if v not in vIndex:
                vIndex[v] = [i]
            else:
                vIndex[v].append(i)
        
        # sort the nums
        nums.sort()

        # do the sum up
        (l, r) = (0, len(nums)-1)
        while nums[l]+nums[r] != target:
            if nums[l]+nums[r] < target:
                l += 1
            else:
                r -= 1
        
        res = []
        res.append(vIndex[nums[l]].pop())
        res.append(vIndex[nums[r]].pop())
        return res

            
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 18))