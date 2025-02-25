# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    '''
    从前序与中序遍历构造二叉树
    '''
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def helper(preorder, inorder):
            if len(inorder) == 0: return
            index = inorder.index(preorder[0])


            curr = TreeNode(val=preorder.pop(0))
            curr.left = helper(preorder, inorder[:index])
            curr.right = helper(preorder, inorder[index+1:])

            return curr # 记得这里要return，否则挂不上
        
        return helper(preorder, inorder)



    @classmethod
    def arrayStorageToTreeNode(self, head):
        ''' 《层次遍历》         --------------------- obsolete -----------------------> see <arrayToTreeNode>
        索引规则（以 0 为起点）：
        - 根节点的索引是 0。
        - 左子节点的索引是 2*i + 1。
        - 右子节点的索引是 2*i + 2。
        '''
        if head == None: return []          # 不好，应该是 if not head: return None

        tnDict = {}
        tn = TreeNode(head[0])
        (tnDict[0], hea) = (tn, tn)
        (i, j) = (0, 0)
        while True:
            if i in tnDict:

                tn = tnDict[i]
                if 2*(i-j)+1 < len(head):
                    if head[2*(i-j)+1] != None: 
                        tn.left = TreeNode(head[2*(i-j)+1])
                        tnDict[2*i+1] = tn.left
                else:
                    break

                if 2*(i-j)+2 < len(head):
                    if head[2*(i-j)+2] != None: 
                        tn.right = TreeNode(head[2*(i-j)+2])
                        tnDict[2*i+2] = tn.right
                else:
                    break
            else:
                j += 1
            i += 1
        return hea

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

    @classmethod
    def treeNodeToArray(cls, root):
        '''
        将二叉树转换为数组表示的形式
        '''
        if not root: return []
        
        res = []
        stack = [root]
        
        while stack:
            curr = stack.pop(0)
            if curr:
                res.append(curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
            else:
                res.append(None)

        # 去掉末尾的 None（因为数组的最后几项可能是多余的空节点）
        while res and res[-1] is None:
            res.pop()

        return res

if __name__ == "__main__":

    
    sol = Solution()

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    res = sol.buildTree(preorder, inorder)


    print (f"res = {res}")

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