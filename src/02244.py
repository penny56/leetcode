#-- coding:utf8 --

'''
Created on Feb 24, 2021

1. 没算出来

@author: mayijie
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p.left != None and q.left != None:
            return isSameNode(p.left, q.left)
        if p.right != None and q.right != None:
            return isSameNode(p.right, q.right)
        if not p and not q:
            return p.val == q.val
        else:
            return False 

if __name__ == "__main__":
    sol = Solution()
    tl1 = TreeNode(2)
    tl2 = TreeNode(3)
    tl = TreeNode(1, tl1, tl2)
    tr1 = TreeNode(2)
    tr2 = TreeNode(3)
    tr = TreeNode(1, tr1, tr2)
    res = sol.isSameTree(tl, tr)