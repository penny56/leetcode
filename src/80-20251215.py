from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        numArr = []
        i = 0
        # dic 的key是nums中的数；dic的value表示这个数出现的次数
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
            
        numArr = list(dic.keys())
        numArr.sort()

        for num in numArr:
            if dic[num] == 1:
                nums[i] = num
                i += 1
            else:
                nums [i] = num
                i += 1
                nums [i] = num
                i += 1
        
        return i+1

if __name__ == '__main__':
    sol = Solution()
    res = sol.removeDuplicates([1,1,1,2,2,3])
    print(f'{res}')

