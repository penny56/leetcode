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
    dfs() 递归
    '''
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minValue = float('inf')

        def dfs(layer, i, sum):
            nonlocal minValue
            
            if layer == len(triangle)-1:
                if sum+triangle[layer][i] < minValue: minValue = sum+triangle[layer][i]
                return

            sum = sum+triangle[layer][i]
            dfs(layer+1, i, sum)
            dfs(layer+1, i+1, sum)

        dfs(layer = 0, i=0, sum=0)
        return minValue

    '''
    动态规划 DP (Dynamic Programming)
    <核心思想>- 将问题分解为子问题，通过存储子问题的解来避免重复计算

    1. 【定义状态】: dp[i][j] 来表示从 顶 到 i行j列 的 最小路径和
    2. 【状态转移方程】: 对每个位置 (i, j) 是从上一行的 (i-1, j-1) 或 (i-1, j) 转移而来，因此转移1程为
       dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
    3. 【初始化】: dp[0][0] = triangle[0][0]
    4. 【边界条件】: 对于每行的第一个元素 只能从上一行的第一个元素移动过来 对每行最后一个(j==i) 只能从上一行最后一个元素移动过来
       dp[i][0] = triangle[i][0] + dp[i-1][0]
       dp[i][j] = triangle[i][j] + dp[i-1][j-1]
    5. 【计算顺序】: 一般是从简单到复杂（或者从小到大）
    6. 【最终结果】: dp数组最后一行的最小值

    '''
    def minimumTotal2(self, triangle):
        dp = [[0] * len(triangle) for _ in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    dp[i][0] = dp[i-1][0]+triangle[i][0]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
        
        return min(dp[i])


        

if __name__ == "__main__":

    
    sol = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    res = sol.minimumTotal2(triangle)
    print(res)
