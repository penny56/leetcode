import itertools

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        s = set()
        res = []
        
        left = ('(',) * n
        right = (')',) * n

        all_permutations = set(itertools.permutations(left+right))
        print (f"all_permutations = {all_permutations}")

        # 输出所有排列
        for tri in all_permutations:
            lt = list(tri)
            print (f"lt = {lt}")
            stack = []
            while len(lt) > 0:
                # get from list head (left side)
                c = lt.pop(0)
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    if not stack:
                        break
                    elif stack[0] == '(':
                        stack.pop(0)
                    elif stack[0] == ')':
                        break
                else:
                    pass
            if len(lt) == 0:
                print ("append")
                res.append(''.join(tri))
        return res

        


sol = Solution()

res = sol.generateParenthesis(3)
print ("res = ", res)





