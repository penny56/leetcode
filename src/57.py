class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        if not intervals:
            return [newInterval]

        merged = []
        mergedAlready = False

        for interval in intervals:
            if not mergedAlready:
                # 未merged
                if interval[0] <= newInterval[0]:
                    # 先进list里的段
                    merged.append(interval)
                    if interval[1] < newInterval[0]:
                        # 处理下一interval
                        pass
                    else:
                        # 需要merge：
                        merged[-1] = [interval[0], max(interval[1], newInterval[1])]
                        mergedAlready = True
                else:
                    # new比较小，先进new
                    merged.append(newInterval)
                    if interval[0] > newInterval[1]:
                        merged.append(interval)
                    else:
                        # 需要merge
                        merged[-1][1] = max(merged[-1][1], interval[1])
                    mergedAlready = True

            else:
                # 还需要考虑当前 interval 是否被 newInterval 包住了
                if merged[-1][1] < interval[0]:
                    # merged尾小于当前头
                    merged.append(interval)
                else:
                    # 当前头小于merged尾
                    merged[-1][1] = max(merged[-1][1], interval[1])

        if not mergedAlready:
            if newInterval[0] > merged[-1][1]:
                # 只要append就好
                merged.append(newInterval)
            else:
                # 需要 merge
                merged[-1][1] = max(merged[-1][1], newInterval[1])
        return merged


sol = Solution()

intervals = [[1,5],[6,8]]
newInterval = [5,6]

res = sol.insert(intervals, newInterval)
print ("res = ", res)





