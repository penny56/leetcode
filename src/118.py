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

    '''
    动态规划 DP (Dynamic Programming)
    <核心思想>- 将问题分解为子问题，通过存储子问题的解来避免重复计算

    1. 【定义状态】: arr[i] 表示三角型当前行，第i列
    2. 【状态转移方程】: 对每个位置 [i] 是从上一行的 [i-1]+[i] 转移而来，因此转移方程为
       arr[i] = (上一行) arr[i-1]+arr[i]
    3. 【初始化】: arr[0] = 1
    4. 【边界条件】: 对于每行的第一个元素 只能从上一行的第一个元素移动过来 对每行最后一个(j==i) 只能从上一行最后一个元素移动过来
       arr[0] = 1
       arr[-1] = 1
    5. 【计算顺序】: 一般是从简单到复杂（或者从小到大）
    6. 【最终结果】: 二维数组
    '''

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            arr = [1]*(i+1)
            if i >= 2:
                for j in range(1, i):   # 去掉 首列 与 尾列
                    arr[j] = prev[j-1]+prev[j]
            res.append(arr)
            prev = arr[:]
        
        return res


        

if __name__ == "__main__":

    
    sol = Solution()
    res = sol.generate(5)
    print(res)
