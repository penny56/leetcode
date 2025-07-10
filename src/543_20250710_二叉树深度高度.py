# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        '''
        当我们说“深度”时，是由根向下，根的深度是0
        当我们说“高度”时，是由叶子向上，叶子的高度是0
        '''

        self.max_diameter = 0

        def dfs(node):
            if not node: return -1 # 空节点的高度定义为-1

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if left_height+right_height+2 > self.max_diameter:
                self.max_diameter = left_height+right_height+2
            
            return max(left_height, right_height) + 1

        dfs(root)

        return self.max_diameter


        
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

if __name__ == "__main__":
    sol = Solution()

    head1 = sol.arrayToTreeNode([1,2,3,4,5])

    res = sol.diameterOfBinaryTree(head1)
    print(res)