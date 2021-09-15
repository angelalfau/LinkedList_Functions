from collections import deque


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def create_linkedlist(queue: deque) -> ListNode:
    head = ListNode(queue.popleft())
    curr = head
    while queue:
        curr.next = ListNode(queue.popleft())
        curr = curr.next
    return head

def create_doublylinkedlist(queue: deque) -> ListNode:
    head = ListNode(queue.popleft())
    curr = head
    prev = None
    while queue:
        curr.next = ListNode(queue.popleft())
        curr.prev = prev
        prev = curr
        curr = curr.next
    curr.prev = prev
    return head
        
def create_circularlinkedlist(queue: deque) -> ListNode:
    head = ListNode(queue.popleft())
    curr = head
    while queue:
        curr.next = ListNode(queue.popleft())
        curr = curr.next
    curr.next = head
    return head

def create_circulardoublylinkedlist(queue: deque) -> ListNode:
    head = ListNode(0)
    curr = head
    prev = None
    while queue:
        curr.next = ListNode(queue.popleft())
        curr.prev = prev
        prev = curr
        curr = curr.next

    curr.next = head.next
    curr.prev = prev
    prev = curr
    curr = curr.next
    curr.prev = prev
    return head.next


def print_linkedlist(head: ListNode, reverse=False) -> None:
    if reverse:
        print("\nPrinting non-circular doubly linked list in reverse\n----------------------------------")
        curr = head
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.val)
            curr = curr.prev
    else:
        print("\nPrinting non-circular linked list\n----------------------------------")
        while head:
            print(head.val)
            head = head.next
    return

def print_circularlinkedlist(head: ListNode, reverse=False) -> None:
    if reverse:
        print("\nPrinting Circular linked list in reverse\n------------------------")
        for i in range(12):
            head = head.prev
            print(head.val)
        return
    print("\nPrinting Circular linked list\n-------------------------")
    for i in range(12):
        print(head.val)
        head = head.next
    return


def reverse_linkedlist(head: ListNode) -> ListNode:
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverse_doublylinkedlist(head: ListNode):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next
    return prev

def reverse_circularlinkedlist(head: ListNode) -> ListNode:
    curr = head
    prev = None
    looped = False
    while curr:
        if curr == head and looped:
            curr.next = prev
            prev = curr
            return prev.next
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        looped = True
    return None

def reverse_circulardoublylinkedlist(head: ListNode) -> ListNode:
    curr = head
    prev = None
    looped = False
    while curr:
        if curr == head and looped:
            curr.next = prev
            prev = curr
            return prev.next
        next = curr.next
        curr.next = prev
        curr.prev = next
        prev = curr
        curr = next
        looped = True
    return None


def insert_listnode(head: ListNode, val: int, rear=False) -> ListNode:
    if rear:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        return head
    # inserts node at the front of a singly linked list
    curr = ListNode(val)
    curr.next = head
    return curr

def insert_circularlistnode(head: ListNode, val: int, doubly=False) -> ListNode:
    curr = head.next
    while curr.next != head:
        curr = curr.next
    curr.next = ListNode(val)
    curr = curr.next
    curr.next = head
    return head

# [x]
def remove_n_node(head: ListNode, val: int, end=False):
    if val < 1:
        print("value inputted less than 1. Returning original linked list...")
        return head
    if end:
        sen = ListNode(0)
        sen.next = head
        first = sen

        while val > 0:
            first = first.next
            val -= 1
        second = sen

        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next

    else:
        sen = ListNode(0)
        sen.next = head
        left = sen
        while val > 1:
            left = left.next
            val -= 1
        left.next = left.next.next
    
    return sen.next

def find_mid(head: ListNode, circular=False):
    low = head
    high = head
    if circular:
        looped = False
        while True:
            if looped and (high == head or high.next == head):
                break
            low = low.next
            high = high.next.next
            looped = True
    else:        
        while high and high.next:
            low = low.next
            high = high.next.next
    print(f"\nThe middle node of the list is: {low.val}\n")
    return low


# to improve,
# work on cases where val is double digits or more  FOR CIRCULAR
# could just make first line into string
# then find length of string
# second line print ^ then " "*len(line1)-2 then v
# third line ???

# make lines 1 and 3 into arrays (e.g. [1,"->",2,"->",3]   and   ' '.join(array) at end)
# take max of len(line1) and len(line3)
# add spaces to make lower line equal to line 3
def model_ll(head: ListNode, circular=False) -> None:
    # case for singly non-circular linked list
    # instead of asking if doubly, check if prev exists ( doubly if curr.next.prev else singly)

    # for circular can check if curr.next or curr.next != head
    if not circular:
        curr = head
        if curr.next.prev:
            arrow = "<-> "
        else:
            arrow = "-> "
        while curr.next:
            print(curr.val, arrow, end="")
            curr = curr.next
        print(curr.val)
    
    # for circular singly
    # if even, print half of values on top, skip a line, and print rest backwards
    # if odd, need more space on bottom
    else:
        if head.prev:
            arrow = " <-> "
            back_arrow = " <-> "
        else:
            arrow = " -> "
            back_arrow = " <- "
        values = [head.val]
        curr = head.next
        while curr != head:
            values.append(curr.val)
            curr = curr.next
        N = len(values)
        print(values[:N//2])

        # 4 * num_arrows + N//2 - 2
        # 4 * (N//2-1) + N//2 - 2
        # N//2 = x
        # 4 * (x-1) + x - 2
        # 4x-6+x
        # 5x-6
        # 5*(N//2)-6

        if N % 2 == 0:
            half = N//2
            # even number of values, so print half on top, rest on bottom
            print(arrow.join(map(str,values[:half])))
            num_spaces = (5*(half))-6
            print("^", " "*num_spaces, "v", sep="")
            print(back_arrow.join(map(str,values[half:][::-1])))
        
        else: 
            # odd number of values, so figure something out
            print("WIP: odd length linked list :( will be implemented shortly")
    return



if __name__ == "__main__":
    # queue = deque([1,2,3,4])
    queue = deque([1,2,3,4,5,6,7,8,9,10])

    head = create_linkedlist(queue.copy())
    # print_linkedlist(head)
    # print_linkedlist(reverse_linkedlist(head))
    # print_linkedlist(insert_listnode(head,9,True))
    # head = remove_n_node(head,1,False)
    # print_linkedlist(head)
    

    dhead = create_doublylinkedlist(queue.copy())
    # print_linkedlist(dhead, True)
    # print_linkedlist(reverse_doublylinkedlist(dhead),True)

    chead = create_circularlinkedlist(queue.copy())
    # print_circularlinkedlist(chead)
    # print_circularlinkedlist(reverse_circularlinkedlist(chead))
    # print_circularlinkedlist(insert_circularlistnode(chead,9))
    
    cdhead = create_circulardoublylinkedlist(queue.copy())
    # print_circularlinkedlist(cdhead,True)
    # print_circularlinkedlist(reverse_circulardoublylinkedlist(cdhead),True)

    # find_mid(chead,True)

    model_ll(chead, True)


# [x] create reverse_linkedlist function
# [ ] create remove_n_node(start/end) # choose if nth from head or nth from end
# [ ] create insert_node(front/back)