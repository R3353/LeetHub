# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #fake starter node essentially; placeholds the start of a node.
        tail = dummy #actually moves along the list. assigning it to dummy only has it start on the starting node.

        #edge case: if l1 and/or l2 is empty
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        #compare the heads of l1 and l2
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 #points tail of dummy LL to the head of l1.
                list1 = list1.next #move pointer of l1 ahead. tail still pointing to what it used to be.
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

            #if one ends earlier than the other
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2

        return dummy.next #.next -ing dummy returns the next node as the head, basically making the first node tail connects to the head :D