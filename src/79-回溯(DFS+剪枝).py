# https://leetcode.cn/problems/word-search/solutions/2361646/79-dan-ci-sou-suo-hui-su-qing-xi-tu-jie-5yui2/
# 回溯 = 深度优先搜索（DFS）+ 剪枝
# DFS 类似树的先根、中根、后根遍历，但是是自己定义顺序。如本题，可以自定义遍历的顺序为：自己->下->上->左->右。
'''
递归参数：
当前元素在矩阵 board 的坐标：x, y，当前字符在 word 中的索引 k。

终止条件：
1. 返回false：
   - 行或列越界
   - 当前矩阵元素与目标元素不同（或已访问过）
2. 返回true：
   - k = len(word)-1，即 word 已全部匹配

递推工作：
1. 标记当前矩阵元素：board[i][j] = ''，避免重复访问
2. 搜索下一单元格，按 上、下、左、右 的顺序，用 ‘或’ 连接，表示只找到一条路径就行，不再作后序的 DFS，并记录结果到 res。
3. 还原当前矩阵元素：board[i][j] = work[k]

返回值：
res = True/False，代表是否找到 word 串

'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or k >= len(word) or board[i][j] != word[k]: return False
            if k == len(word)-1: return True
                
            # 自己
            elem = board[i][j]
            board[i][j] = ''
            res = dfs(i, j+1, k+1) or dfs(i, j-1, k+1) or dfs(i-1, j, k+1) or dfs(i+1, j, k+1)
            board[i][j] = elem
            return res


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, k=0):
                    return True
        
        return False
        


sol = Solution()

print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))