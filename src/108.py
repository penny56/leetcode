# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, arr):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not arr: return None

        elif len(arr) == 3:
            l = TreeNode(val = arr[0])
            r = TreeNode(val = arr[2])
            root = TreeNode(val=arr[1], left=l, right=r)
        elif len(arr) == 2:
            l = TreeNode(val = arr[0])
            root = TreeNode(val=arr[1], left=l)
        elif len(arr) == 1:
            root = TreeNode(val=arr[0])
        else:
    
            half = len(arr)//2
            left = self.sortedArrayToBST(arr[:half])
            right = self.sortedArrayToBST(arr[half+1:])
            root = TreeNode(val=arr[half], left=left, right=right)
        print(f"root = {root}")
        return root




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



if __name__ == "__main__":
    pArray = [1,3]
    sol = Solution()
    res = sol.sortedArrayToBST(pArray)
    print (f"res = {res}")
