# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        '''
        索引规则（以 0 为起点）：
        - 根节点的索引是 0。
        - 左子节点的索引是 2*i + 1。
        - 右子节点的索引是 2*i + 2。
        '''
        if root == None: return []
        # tnDect = {<index> : <node>}
        tnDict = {}
        tn = TreeNode(root[0])
        (tnDict[0], head) = (tn, tn)
        (i, j) = (0, 0)
        while True:
            if i in tnDict:

                tn = tnDict[i]
                if 2*(i-j)+1 < len(root):
                    if root[2*(i-j)+1] != None: 
                        tn.left = TreeNode(root[2*(i-j)+1])
                        tnDict[2*i+1] = tn.left
                else:
                    break

                if 2*(i-j)+2 < len(root):
                    if root[2*(i-j)+2] != None: 
                        tn.right = TreeNode(root[2*(i-j)+2])
                        tnDict[2*i+2] = tn.right
                else:
                    break
            else:
                j += 1
            
            i += 1

        arr = []
        self.midOrder(head, arr)

        return arr

    def midOrder(self, root, arr):

        # if root == None: return
        # self.midOrder(root.left, arr)
        # arr.append(root.val)
        # self.midOrder(root.right, arr)


        # stack 中的元素是一个tuple： (<color>, <treeNode>)
        # color 表示有没有访问过：
        #        - white 表示没有访问，需要优先处理左右子树。
        #        - gray 表示访问过了，直接写入或者显示吧。
        (white, gray) = (0, 1)                          #1. 定义颜色
        stack = [(white, root)]                         #2. 定义栈，并初始化
        while stack:                                    #3. Loop
            (color, curr) = stack.pop()                 #4. 出栈
            if curr:                                    #5. 判断是否是一个节点？
                # 是个非空节点，按颜色处理吧：
                if color == white:                      # 注意这里要 append() 的是一个 tuple ，要双括号->
                    stack.append((white, curr.right))   # 放栈底
                    stack.append((gray, curr))          # 放中间，访问过啦。
                    stack.append((white, curr.left))    # 放栈顶
                else:
                    arr.append(curr.val)

if __name__ == "__main__":
    root = [1,2,3,4,5,None,8,None,None,6,7,9]
    sol = Solution()
    res = sol.inorderTraversal(root)
    print (f"res = {res}")
