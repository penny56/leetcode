class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 依照每个 interval 的 start_i 排序
        intervals.sort(key=lambda interval : interval[0])

        res = [intervals.pop(0)]

        for interval in intervals:
            if interval[0] <= res[-1][1]:
                # 如果这个interval 的start，小于或等于 res中最后一个元素的 end
                # do merge
                # start端，既然是原来排过序了，肯定是res[-1][0]的小
                # end端，就要从 res[-1] 与 interval 2者中取较大值
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]

            else:
                # 如果这个 interval 的 start，大于 res最后一个元素的 end
                # 把这个 interval 加入到 res 数组
                res.append(interval)

        return res
        
