# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
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

        dic = {}
        (dic['curr'], dic['max']) = (0, 0)

        self.midOrder(head, dic)

        return dic["max"]

    def midOrder(self, root, dic):
        
        

        if root == None: return
        self.midOrder(root.left, dic)
        print(f"val = {root.val}")
        dic['curr'] += 1
        if dic['curr'] > dic['max']:
            dic['max'] = dic['curr']
            print(f"curr = {dic['curr']} max = {dic['max']}")
        self.midOrder(root.right, dic)

        dic['curr'] -= 1



if __name__ == "__main__":
    root = [1,2,3]
    sol = Solution()
    res = sol.maxDepth(root)
    print (f"res = {res}")
