# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create a new linked list, make vals = number added together. if a number is greater than 9, floor it by 10 (because any single-digit number added together can at most be 9+9=18)  (EDIT: THIS IS FALSE because let's say there's 9+9 + a carry of 2. i'll just say floor != 0) and then add 1 to the next node's value.
        #however... this IS a recursion problem... i think i am doing the iterative version of linked list. i will watch a video on the LL recursion algo.

        dummy = ListNode(0) #CREATE THE LINKED LIST. dummy for null before head. initialize default val to 0
        curr = dummy #start at dummy :D
        carry = 0

        while l1 != None or l2 != None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            digitSum = val1 + val2 + carry
            carry = digitSum // 10
            curr.next = ListNode(digitSum % 10)
            curr = curr.next #actually move to the next node now.
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry: #if there is leftover digit by the end of the list digit adding
            curr.next = ListNode(carry)

        return dummy.next