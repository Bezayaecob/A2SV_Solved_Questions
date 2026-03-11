# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals=[]
        curr=head
        while curr:
            vals.append(curr.val)
            curr=curr.next

        
        stack=[]
        
        for val in vals: 
            while stack and stack[-1] < val:
                stack.pop()
            stack.append(val)

        
        dummy= ListNode(0)
        curr= dummy
        for val in stack:
            curr.next= ListNode(val)
            curr=curr.next

        return dummy.next