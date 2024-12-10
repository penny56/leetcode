class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        startMin = 65535
        endMax = 0
        for arr in intervals:
            if min(arr[0], arr[-1]) < startMin: startMin = min(arr[0], arr[-1])
            if max(arr[0], arr[-1]) > endMax: endMax = max(arr[0], arr[-1])
        
        dic = dict()
        for i in range(startMin, endMax+1):
            dic[i] = 0
        
        for arr in intervals:
            for i in range(arr[0], arr[-1]+1):
                dic[i] = 1
        # print(f"dic = {dic}")
        
        res = []
        temp = []
        temp.insert(0, startMin)
        recording = True
        for i in range(startMin, endMax+1):
            if dic[i] == 1 and not recording:
                temp.insert(0, i)
                recording = True
            if dic[i] == 0 and recording:
                temp.insert(1, i-1)
                tempCopy = temp[:]
                res.append(tempCopy)
                temp = []
                recording = False
        
        temp.insert(1, endMax)
        res.append(temp)

        return res




sol = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
res = sol.merge(intervals)
print ("res = ", res)





