class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        dic = {}
        startArr = []

        for interval in intervals:
            if interval[0] not in dic.keys():
                dic[interval[0]] = interval
            else:
                dic[interval[0]] = max(interval, dic[interval[0]])
        
        startArr = sorted(list(dic.keys()))

        oldArr = dic[startArr.pop(0)]

        while startArr:
            currArr = dic[startArr.pop(0)]
            if currArr[0] <= oldArr[-1]:
                # 可 merge
                oldArr[-1] = max(oldArr[-1], currArr[-1])
            else:
                # 不可merge
                res.append(oldArr)
                oldArr = currArr
        
        res.append(oldArr)
        
        return res  


sol = Solution()
print(sol.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))