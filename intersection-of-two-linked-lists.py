# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        pointa = headA
        pointb = headB

        while pointa != pointb:
            pointa = pointa.next if pointa else headB
            pointb = pointb.next if pointb else headA

        return pointa
