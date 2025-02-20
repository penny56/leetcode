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

    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root: return 0
        minValue = float('inf')
        def dfs(root, dep):
            nonlocal minValue
            if not root: return
            dep += 1
            if not root.left and not root.right:
                if dep < minValue: minValue = dep
            dfs(root.left, dep)
            dfs(root.right, dep)
        dfs(root, 0)
        return minValue




if __name__ == "__main__":

    sol = Solution()
    head = []
    root = sol.arrayToTreeNode(head)

    res = sol.minDepth(root)


    print (f"res = {res}")
