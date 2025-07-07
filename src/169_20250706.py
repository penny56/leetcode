class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        # 创建一个key是num, value是cnt的dict
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
        
        valueCnts = list(dic.values())
        maxCnt = sorted(valueCnts)[-1]

        for k, v in dic.items():
            if v == maxCnt: return k


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,3,4]))