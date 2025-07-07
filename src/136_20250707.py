class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num in dic.keys():
                del dic[num]
            else:
                dic[num] = 1
        return dic.keys()[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([3,3,4]))