class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=ListNode()
        fast=ListNode()
        slow=head
        fast=head
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
            if fast.next is not None:
                fast=fast.next
        return slow
