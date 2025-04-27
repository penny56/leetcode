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
    
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return None

        tail = ListNode(0)
        tailLn = tail
        
        # 外循环，每个loop找到自己的尾巴
        while head.next:
            ln = head
            while ln.next:
                prev = ln
                ln = ln.next
            tailLn.next = ln
            tailLn = tailLn.next
            prev.next = None

        tailLn.next = head
        return tail.next
        
                
        
            
if __name__ == "__main__":
    sol = Solution()

    head = sol.arrToListNode([1])
 
    print(sol.reverseList(head))
