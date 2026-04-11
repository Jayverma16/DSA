import time
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
        # Check if there are at least k nodes remaining
        count = 0
        node = head
        while node and count < k:
            node = node.next
            count += 1
        
        # If fewer than k nodes remain, return head as-is
        if count < k:
            return head
        
        # Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # head is now the tail of the reversed group
        # Recursively process the rest and connect
        head.next = reverseKGroup(curr, k)
        
        # prev is now the new head of the reversed group
        return prev

if __name__ == "__main__":
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)

    # dummy = ListNode(0)
    # dummy.next = head
    example_list = [1,2,3,4,5,6]
    head = None
    previous = None
    for i,val in enumerate(example_list):
        if not i:
            head = ListNode(val)
            previous = head
            continue
        previous.next = ListNode(val)
        previous = previous.next

        
    # print(dummy.val)         # 0
    # print(dummy.next.val) 
    # result = reverse_thing(head.next, head.next.next)
    # head.next = next_attach
    # print(result.val)
    # print(result.next.val)
    # print(result.next.next.val)

    result = reverseKGroup(head=head, k=2)
    current = result   
    while  current:
        print(current.val)
        current = current.next
        time.sleep(1)


        