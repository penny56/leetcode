'''
全局变量：
candidates[]: 
res[]:

递归参数：
path[]: 当前branch已走过的路径
target: 当前递归要找到的目标数

终止条件：
1. target < 0: 返回
2. target == 0: path入栈


递推工作：
1. 遍历candidates[]，如果< target的，就递归


返回值：
None

'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort(reverse=True)

        def dfs(path, target):
            if target == 0:
                res.append(path[:])
                return
            for candidate in candidates:
                if candidate <= target:
                    path.append(candidate)
                    dfs(path, target-candidate)
                    path.pop()
        
        dfs(path=[], target=target)

        # 消除重复
        s = set()
        for r in res:
            s.add(tuple(sorted(r)))
        res.clear()
        for uni in s:
            res.append(list(uni))

        return res
            


sol = Solution()


print(sol.combinationSum(candidates = [2,3,6,7], target = 7))