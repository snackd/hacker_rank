# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        l1, l2 = headA, headB

        l1_len, l2_len = 0, 0

        while not l1:
            l1_len += 1
            l1 = l1.next
        while not l2:
            l2_len += 1
            l2 = l2.next

        diff = l1_len - l2_len
practice
        l1, l2 = headA, headB
        if diff > 0:
            for _ in range(diff):
                l1 = l1.next
        else:
            for _ in range(-diff):
                l2 = l2.next

        while l1 and l2:
            if l1 == l2:
                return l1
            l1, l2 = l1.next, l2.next
        return l1

        # while l1 != l2:
        #     l1 = l1.next if l1 else headB
        #     l2 = l2.next if l2 else headA
        # return l1
