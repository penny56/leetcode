# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    @classmethod
    def arrayToTreeNode(cls, head):
        ''' 《层次遍历》
        索引规则（以 0 为起点）：
        - 根节点的索引是 0。
        - 左子节点的索引是 2*i + 1。
        - 右子节点的索引是 2*i + 2。
        '''
        if not head: return None
        
        # 创建根节点
        root = TreeNode(head[0])
        stack = [root]
        i = 1
        while i < len(head):
            curr = stack.pop(0)     # 队列，先进先出
            
            # 左子节点
            if i < len(head) and head[i] is not None:   # 不越界，且不为空
                curr.left = TreeNode(head[i])
                stack.append(curr.left)
            i += 1

            # 右子节点
            if i < len(head) and head[i] is not None:
                curr.right = TreeNode(head[i])
                stack.append(curr.right)
            i += 1
        
        return root

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def midOrder(root, sum):
            if not root: return False

            nonlocal targetSum

            sum += root.val
            if sum == targetSum and not root.left and not root.right:
                return True
            if midOrder(root.left, sum): return True
            if midOrder(root.right, sum): return True
            sum -= root.val

            return False
        
        return midOrder(root, 0)

    '''
    GPT 建议优化之后的
    '''
    def hasPathSum2(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        res = []
        def midOrder(root, sum, path):
            if not root: return
            path.append(root.val)

            sum += root.val
            if not root.left and not root.right and sum == targetSum:
                res.append(path[:]) # 这里一定是“深复制”，不能用引用复制

            midOrder(root.left, sum, path)
            midOrder(root.right, sum, path)
            path.pop()
        
        midOrder(root, 0, [])
        return res

if __name__ == "__main__":

    
    sol = Solution()
    head = [-2,None,-3]
    root = Solution.arrayToTreeNode(head)
    res = sol.hasPathSum2(root, targetSum = -5)
    print(res)

'''
Get the markdown chat from GPT
head = [1,2,3,4,5,None,8,None,None,6,7,9]

         1
       /   \
      2     3
     / \      \
    4   5      8
       / \    /
      6   7  9

正确的遍历顺序：
中序 = [4, 2, 6, 5, 7, 1, 3, 9, 8]
先根 = [1, 2, 4, 5, 6, 7, 3, 8, 9]
后根 = [4, 6, 7, 5, 2, 9, 8, 3, 1]
层次 = [1, 2, 3, 4, 5, 8, 6, 7, 9]
层次withLevelOutput = [[1], [2, 3], [4, 5, 8], [6, 7, 9]]
'''