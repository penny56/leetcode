class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0: return 0
        sortedList = sorted(list(set(nums)))
        (currLength, maxLength) = (1, 1)
        
        for i, num in enumerate(sortedList):
            if i == 0:
                lastOne = num
                continue
            else:
                if num == lastOne+1:
                    currLength += 1
                else:
                    if currLength > maxLength:
                        maxLength = currLength
                    currLength = 1
                lastOne = num
        
        return max(currLength, maxLength)


        

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))