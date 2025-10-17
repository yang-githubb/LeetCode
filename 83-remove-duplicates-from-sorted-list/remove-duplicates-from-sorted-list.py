# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        Removes duplicates from a sorted linked list in-place.
        """
        curr = head                       # 1. start pointer at head
        while curr and curr.next:         # 2. iterate while there is a current node and a next node
            if curr.val == curr.next.val: # 3. if duplicate found
                curr.next = curr.next.next# 4. skip the next node (remove duplicate)
            else:
                curr = curr.next          # 5. otherwise advance curr
        return head                       # 6. return the (possibly modified) head

# --- Helper utilities for testing ---
def list_to_linkedlist(arr):
    """Convert Python list to linked list and return head."""
    if not arr:
        return None
    head = ListNode(arr[0])
    tail = head
    for v in arr[1:]:
        tail.next = ListNode(v)
        tail = tail.next
    return head

def linkedlist_to_list(head):
    """Convert linked list back to Python list for easy printing."""
    out = []
    curr = head
    while curr:
        out.append(curr.val)
        curr = curr.next
    return out