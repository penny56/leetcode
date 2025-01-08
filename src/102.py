# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
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

        if not head: return []
        arr = []
        arr.append(head)

        res = []
        level = []
        currsize = 1
        nextsize = 0
        while len(arr) != 0:
            node = arr.pop(0)
            level.append(node.val)

            if node.left:
                nextsize += 1
                arr.append(node.left)
            if node.right:
                nextsize += 1
                arr.append(node.right)

            if len(level) == currsize:
                res.append(level)
                level = []
                currsize = nextsize
                nextsize = 0
        return res



if __name__ == "__main__":
    root = [1,2,3,4,5,None,6,None,None,7,None,8,9]
    sol = Solution()
    res = sol.levelOrder(root)
    print (f"res = {res}")
