# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @classmethod
    def arrToListNode(self, arr):
        head = ln = ListNode(0)

        for i in range(len(arr)):
            curr = ListNode(arr[i])
            ln.next = curr
            ln = ln.next
        return head.next
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        (ln, lnSet) = (head, set())

        while ln:
            if ln in lnSet:
                return True
            else:
                lnSet.add(ln)
            ln = ln.next

        return False


if __name__ == "__main__":
    sol = Solution()

    head = sol.arrToListNode([1,2,3])
 
    print(sol.hasCycle(head))
