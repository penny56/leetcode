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
    
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0)
        (ln, ln1, ln2) = (res, list1, list2)

        while ln1 and ln2:
            if ln1.val <= ln2.val:
                ln.next = ln1
                ln1 = ln1.next
            else:
                ln.next = ln2
                ln2 = ln2.next
            ln = ln.next
        
        if not ln1:
            ln.next = ln2
        else:
            ln.next = ln1
        
        return res.next
            

        


if __name__ == "__main__":
    sol = Solution()

    head1 = sol.arrToListNode([1,2,4])
    head2 = sol.arrToListNode([1,3,4])
 
    res = sol.mergeTwoLists(head1, head2)
    print(res)