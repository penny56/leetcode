from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        while val in nums:
                i = nums.index(val)
                nums = nums[:i]+nums[i+1]
        
        print(f'{nums}')
        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    res = sol.removeElement([0,1,2,2,3,0,4,2], 2)

    print(f'{res}')
