# Singly Linked List Definition
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def solve(head):
  if head.next == None:
    return head

  prev = None
  curr = head
  next = curr.next
  while curr != None:
    next = current.next
    curr.next = prev
    prev = curr
    curr = next

  return curr
# this is honestly so emberassing,
# i have how much time programing, and i cant even reverse a linked list,
# what have I been doing?
#
# Its a good thing i find out here and not in a interview
