# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    '''
    递归算法（前，中，后）
    '''
    def recursive(self, root):
        res = []

        '''
        嵌套函数（nested function）/ 内部函数（Inner function）/ 递归函数（recursive)
        【注意：这个内部函数没有返回值，它只是去给外部的 res 赋值（res无法定义在递归函数内部，因为每次递归会被清零）】
        '''
        def doMidOrder(root):

            if not root: return 
            
            doMidOrder(root.left)
            res.append(root.val)
            doMidOrder(root.right)

        doMidOrder(root)

        return res
    
    '''
    迭代算法（前，中，后）
    '''
    def midOrder(self, root):

        # stack 中的元素是一个tuple： (<color>, <treeNode>)
        # color 表示有没有访问过：
        #        - white 表示没有访问，需要优先处理左右子树。
        #        - gray 表示访问过了，直接写入或者显示吧。
        res = []                                        #0. 定义返回值
        (white, gray) = (0, 1)                          #1. 定义颜色
        stack = [(white, root)]                         #2.1 定义栈，并初始化
        while stack:                                    #2.2 Loop
            (color, curr) = stack.pop()                 #2.3 出栈
            if curr:                                    #3. 判断是否是一个节点？
                if color == white:                      #4. 判断颜色
                    stack.append((white, curr.right))   # 放栈底 【注意反序】【注意这里要 append() 的是一个 tuple ，要双括号->】
                    stack.append((gray, curr))          # 放中间，访问过啦。
                    stack.append((white, curr.left))    # 放栈顶
                else:
                    res.append(curr.val)
                    pass
        return res

    '''
    迭代算法（层次遍历没有递归算法）
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
    迭代算法（层次遍历没有递归算法）
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

    @classmethod
    def arrayStorageToTreeNode(self, head):
        '''
        索引规则（以 0 为起点）：
        - 根节点的索引是 0。
        - 左子节点的索引是 2*i + 1。
        - 右子节点的索引是 2*i + 2。
        '''
        if head == None: return []
        # tnDect = {<index> : <node>}
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

if __name__ == "__main__":
    head = [1,2,3,4,5,None,8,None,None,6,7,9]

    # 把数组存储方式 [1,2,3,4,5,None,8,None,None,6,7,9]，改为 TreeNode 方式
    root = Solution.arrayStorageToTreeNode(head)
    
    sol = Solution()
    res = sol.recursive(root)
    #res = sol.midOrder(root)
    #res = sol.levelOrder(root)
    #res = sol.levelOrderWithLevelOutput(root)
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