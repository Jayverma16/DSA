# Definition for singly-linked list.
import time
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        shift = True
        current = head
        while(current):

            if shift:
                shift = False
                #get the last member
                if current.next:
                    last = current.next
                    prev = current
                    while(last and last.next):
                        # print(last.val)
                        prev = last
                        last = last.next

                    prev.next = None
                    current_next_one = current.next
                    current.next = last
                    last.next = current_next_one
            else:
                shift = True
            current = current.next
            
        return head

                
if __name__ == "__main__":

    example_list = [1,2,3,4,5]
    head = None
    previous = None
    for i,val in enumerate(example_list):
        if not i:
            head = ListNode(val)
            previous = head
            continue
        previous.next = ListNode(val)
        previous = previous.next

    sol = Solution()

    result = sol.reorderList(head=head)
    current = result   
    while  current:
        print(current.val)
        current = current.next
        time.sleep(1)


        
        