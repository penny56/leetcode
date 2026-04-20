# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # 其实无所谓先根、中根、后根遍历，如果发现是叶子节点，入栈

        # 这里使用后根
        def helper(root: Optional[TreeNode], stack: []) -> None:
            if not root: return
            helper(root.left, stack)
            helper(root.right, stack)
            if not root.left and not root.right:
                stack.append(root.val)
            
            return
        
        (s1, s2) = ([], [])

        helper(root1, s1)
        helper(root2, s2)

        if s1 == s2:
            return True
        else:
            return False
