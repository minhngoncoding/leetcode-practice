class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        nxt = None
        curr = head

        while curr:
            if not curr.next:
                head = curr
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return head