class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        print(f"candidates = {candidates}")



sol = Solution()
candidates = [2,3,6,7]
target = 7

res = sol.combinationSum(candidates, target)
print ("res = ", res)





