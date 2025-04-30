# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def copy_tree(node):
            if node is None:
                return None

            new_node = TreeNode(node.val)
            new_node.left = copy_tree(node.left)
            new_node.right = copy_tree(node.right)
            return new_node

        # 把原树复制一下
        dup_root = copy_tree(root)

        def invertTree(root):
            if not root: return

            invertTree(root.left)
            invertTree(root.right)

            tn = root.left
            root.left = root.right
            root.right = tn

            return root
        
        # 把原树反转一下
        rev_root = invertTree(root)

        def is_same_tree(p, q):
            if not p and not q:
                return True  # 都为空，返回 True
            if not p or not q:
                return False  # 一个为空一个不为空，返回 False
            if p.val != q.val:
                return False  # 值不同，返回 False

            # 递归判断左右子树
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        # 对比复制树与反转树
        return is_same_tree(dup_root, rev_root)



        
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

    head1 = sol.arrayToTreeNode([1,2,2,None,3,None,3])

    res = sol.isSymmetric(head1)
    print(res)