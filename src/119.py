'''
递归参数：
layer: 当前是哪一层(塔尖 layer = 0)
i: 当前index（哪一列/横轴）
sum: 截止到当前层的总合

终止条件：
1.当前层是最底层 layer == len(triangle)-1

递推工作：
maxValue = 最小值
1. 


返回值：
无

'''

class Solution(object):


    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(rowIndex):
            arr = [1]*(i+1)
            if i >= 2:
                for j in range(1, i):   # 去掉 首列 与 尾列
                    arr[j] = prev[j-1]+prev[j]
            prev = arr[:]
        
        return arr


        

if __name__ == "__main__":

    
    sol = Solution()
    res = sol.getRow(3)
    print(res)
