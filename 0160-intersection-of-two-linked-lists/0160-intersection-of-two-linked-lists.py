# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptra= headA
        ptrb=headB
        while ptra!=ptrb:
            if ptra:
                ptra= ptra.next
            else:
                ptra=headB
            if ptrb:
                ptrb=ptrb.next
            else:
                ptrb=headA
        return ptrb