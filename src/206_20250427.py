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
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        setA = set()
        # put nodes in listA to setA
        ln = headA
        while ln:
            setA.add(ln)
            ln = ln.next
        
        # go throught listB, if NodeB in the setA, return NodeB
        ln = headB
        while ln:
            if ln in setA:
                return ln
            ln = ln.next
        
        # return None if not return yet
        return None

            
if __name__ == "__main__":
    sol = Solution()

    headA = sol.arrToListNode([4,1,8,4,5])
    headB = sol.arrToListNode([5,6,1,8,4,5])
 
    print(sol.getIntersectionNode(headA, headB).val)
