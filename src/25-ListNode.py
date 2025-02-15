# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @classmethod
    def arrToListNode(self, arr):
        head = ln = ListNode(0)

        for i in range(len(arr)):
            curr = ListNode(arr[i])
            ln.next = curr
            ln = ln.next
        return head.next
        
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        res = []
        (eStack, iStack) = ([], [])
        ln = head
        i = 0
        while ln:
            iStack.append(ln.val)
            if i%k == k-1:
                eStack.append(iStack)
                iStack = []
            ln = ln.next
            i += 1
        
        if len(iStack) < k:
            eStack.append(iStack[::-1])
        
        for iStack in eStack:
            for node in iStack[::-1]:
                res.append(node)
        
        return res
        

sol = Solution()

arr = [1,2,3,4,5]

head = Solution.arrToListNode(arr)

res = sol.reverseKGroup(head = head, k = 3)

print(res)