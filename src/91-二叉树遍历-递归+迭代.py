# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    '''
    递归算法（前，中，后），【res】用嵌套函数实现。
    '''
    def midOrder(self, root):
        res = []

        '''
        嵌套函数（nested function）/ 内部函数（Inner function）/ 递归函数（recursive)
        【注意1：这个内部函数没有返回值，它只是去给外部的 res 赋值（res无法定义在递归函数内部，因为每次递归会被清零）】
        【注意2：这个内部函数的第一个参数 不需要 是self】
        '''
        def helper(root):

            if not root: return 
            
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)

        return res
    '''
    递归算法（前，中，后），【res】用传入参数实现。
    '''
    def midOrder(self, root, arr):
        
        if not root: return arr

        self.midOrder(root.left, arr)
        arr.append(root.val)
        self.midOrder(root.right, arr)

        return arr

    '''
    迭代算法（前，中，后）
    '''
    def midOrder(self, root):

        # stack 中的元素是一个tuple： (<color>, <treeNode>)
        # color 表示有没有访问过：
        #        - white 表示没有访问，仍需递归访问子节点。(第一次到达)
        #        - gray 子节点已经访问过，现在可以访问该节点值。(第二次到达)
        res = []                                        #0. 定义返回值
        (white, gray) = (0, 1)                          #1. 定义颜色
        stack = [(white, root)]                         #2.1 定义栈，并初始化
        while stack:                                    #2.2 Loop
            (color, curr) = stack.pop()                 #2.3 出栈
            if curr:                                    #3. 判断是否是一个节点？
                if color == white:                      #4. 判断颜色（第一次到达）
                    stack.append((white, curr.right))   # 放栈底 【注意反序】【注意这里要 append() 的是一个 tuple ，要双括号->】
                    stack.append((gray, curr))          # 放中间，访问过啦。
                    stack.append((white, curr.left))    # 放栈顶
                else:                                   # 第二次到达（此时左子树已访问）。
                    res.append(curr.val)

        return res

    '''
    迭代算法（层次遍历没有递归算法）
    【注意：】层次遍历不需要回溯（这点与前中后序遍历不同），所以不需要color变量。
    '''
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        res = []                            #0. 定义返回值
        stack = [root]                      #2.1 定义栈，并初始化

        # 进行层序遍历
        while stack:                        #2.2 Loop
            curr = stack.pop(0)             #2.3 出栈（需要一个Queue，先进先出，这里用stack.pop(0)来代替）
            if curr:                        #3. 判断是否是一个节点？
                res.append(curr.val)        #4. curr -> 左进栈 -> 右进栈
                stack.append(curr.left)
                stack.append(curr.right)

        return res

    '''
    迭代算法（层次输出）（层次遍历没有递归算法）
    '''
    def levelOrderWithLevelOutput(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        res = []                            #0. 定义返回值
        stack = [root]                      #2.1 定义栈，并初始化

        # 进行层序遍历
        while stack:                        #2.2 Loop
            
            level = []
            levelSize = len(stack)
            j = 0
            while j < levelSize:
                
                curr = stack.pop(0)             #2.3 出栈（需要一个Queue，先进先出，这里用stack.pop(0)来代替）

                if curr:                        #3. 判断是否是一个节点？
                    level.append(curr.val)        #4. curr -> 左进栈 -> 右进栈
                    stack.append(curr.left)
                    stack.append(curr.right)
                j += 1
            
            res.append(level)

        return res

    '''
    是否是二叉搜索树
    '''
    def is_valid_bst(root):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node: return True
            if not lower <= node.val <= upper: return False     # 1) 检查当前
            if not helper(node.left, lower, node.val): return False     # 2) 检查左子树
            if not helper(node.right, node.val, upper): return False    # 3) 检查右子树
            return True
        return helper(root)

    '''
    构建平衡搜索二叉树（递归）
    arr: 一个有序数组
    '''
    def sortedArrayToBST(self, arr):
        if len(arr) == 0: return

        mid = len(arr)//2                                       #1. 找 root（中间点）

        root = TreeNode(val=arr[mid])                           #2. 创建 root
        root.left = self.sortedArrayToBST(arr[:mid])            #3. 递归的用左边数组的 [:mid] 去创建 root.left
        root.right = self.sortedArrayToBST(arr[mid+1:])         #4. 递归的用右边数组的 [mid+1:] 去创建 root.right

        return root

    '''
    是否平衡二叉树
    '''
    def isBalanced(self, root):

        if not root: return True                                            #0. 返回条件

        def height(root):                                                   #1. 定义嵌套函数 Height() 
            
            if not root: return 0                                           #1.1 如果根为空，返回0
            return 1 + max(height(root.left), height(root.right))           #1.2 返回左、右子树的高度+1 

        leftHeight = height(root.left)                                      #2. 得到左、右子树的高度
        rightHeight = height(root.right)

        return abs(leftHeight - rightHeight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) #3. 左右子树的高度差不高于1 && 左子树 平衡 && 右子树平衡
    
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
    
    '''
    从中序与后序遍历构造二叉树
    '''
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        def helper(inorder, postorder):
            if len(inorder) == 0: return
            index = inorder.index(postorder[-1])


            curr = TreeNode(val=postorder.pop(-1))
            curr.right = helper(inorder[index+1:], postorder)
            curr.left = helper(inorder[:index], postorder)

            return curr
        
        return helper(inorder, postorder)




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
    head = [1,2,3,4,5,None,8,None,None,6,7,9]

    # 平衡二叉树
    head2 = [3,9,20,None,None,15,7]

    nums = [-10,-3,0,5,9]
    nums = [1, 3]

    # 把数组存储方式 [1,2,3,4,5,None,8,None,None,6,7,9]，改为 TreeNode 方式
    # root = Solution.arrayStorageToTreeNode(head)
    # root = Solution.arrayToTreeNode(head2)
    
    sol = Solution()

    # 遍历二叉树（递归）
    #res = sol.recursive(root)

    # 遍历二叉树（递归+传参）
    #arr = []
    #res = sol.midOrderWithParams(root, arr)

    # 遍历二叉树（迭代）
    #res = sol.midOrder(root)

    # 层次遍历二叉树（迭代）
    #res = sol.levelOrder(root)
    
    # 层次遍历二叉树（迭代）（按层次二维输出）
    #res = sol.levelOrderWithLevelOutput(root)
    
    # 有序数组 构建 平衡搜索二叉树（递归）
    #res = sol.sortedArrayToBST(nums2)
    
    # 检测是否是平衡二叉树（递归）
    # res = sol.isBalanced(root)

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