# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        # head 指向自己
        # head.next 指向下一個
        # prev 指向前一個
        while head:
            # 暫存 = 指向下一個
            next = head.next
            # 指向下一個 = 指向前一個
            head.next = prev
            # 指向前一個 = 指向自己
            prev = head
            # 自己 = 暫存的指向下一個
            head = next

        return prev
