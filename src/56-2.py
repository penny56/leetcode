class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        dic = dict()

        # 把intervals里的内容存入 dic
        for arr in intervals:
            if arr[0] in dic.keys():
                dic[arr[0]] = max(dic[arr[0]], arr[1])
            else:
                dic[arr[0]] = arr[1]
        
        # 按 start 排序
        startSorted = list(dic.keys())
        startSorted.sort()

        intervalsSorted = []

        # 把排序后的dict恢复成list
        for start in startSorted:
            intervalsSorted.append([start, dic[start]])

        print(f"intervalSorted = {intervalsSorted}")
                
        merged = []
        rightIndex = 0
        for interval in intervalsSorted:
            if interval[0] == 0 or interval[0] > rightIndex:
                # 如果新段开头在更右
                merged.append(interval)
                rightIndex = interval[1]
            else:
                # 新开关在上一个之内，需要merge
                merged[-1][1] = max(merged[-1][1], interval[1])
                rightIndex = max(merged[-1][1], interval[1])
        
        return merged


sol = Solution()

intervals = [[1,4],[1,5]]
res = sol.merge(intervals)
print ("res = ", res)





