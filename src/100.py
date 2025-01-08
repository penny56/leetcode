# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, pArr, qArr):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        p = self.arrToTree(pArr)
        q = self.arrToTree(qArr)
        dic = {}
        dic['0'] = True # 这里使用 dic['0'] 当一个“桥梁”，因为当形参是字典类型时，可以“回传”参数；而 int, bool 则不行。
        self.midOrder(p, q, dic)
        return dic['0']
    
    def arrToTree(self, root):
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
        return head


    def midOrder(self, p, q, dic):
        
        if not dic['0']:
            return
        if p == None and q == None:
            return
        if p == None or q == None:
            dic['0'] = False
            return
        self.midOrder(p.left, q.left, dic)
        if p.val != q.val:
            dic['0'] = False
            return
        self.midOrder(p.right, q.right, dic)
        return


if __name__ == "__main__":
    pArray = [2,1,3]
    qArray = [2,3]
    sol = Solution()
    res = sol.isSameTree(pArray, qArray)
    print (f"res = {res}")
