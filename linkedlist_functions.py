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
def model_ll(head: ListNode) -> None:

    # for circular can check if curr.next or curr.next != head
    if not head:
        print("Error: Invalid Linked List.")
        return
    curr = head.next
    doubly = False
    circular = False
    
    # if this value != None, then linked list is doubly
    if curr.prev:
        doubly = True
        arrow = " <-> "
        back_arrow = " <-> "
    else:
        arrow = " -> "
        back_arrow = " <- "

    # adding all values of linked list into the [values]
    values = [head.val]
    while curr != head and curr:
        values.append(curr.val)
        curr = curr.next

    # if we returned to the head, then linked list is circular
    if curr == head:
        circular = True

    # handles singly and doubly linked lists (non-circular)
    if not circular:
        print(arrow.join(map(str,values)))
    
    # for circular singly
    # if even, print half of values on top, skip a line, and print rest backwards
    # if odd, need more space on bottom
    else:
        N = len(values)
        print(values[:N//2])


        #          finding num_spaces for 2nd line of result for:
        #         singly                             doubly
        # 4 * num_arrows + N//2 - 2   |    5 * num_arrows + N//2 - 2
        #  4 * (N//2-1) + N//2 - 2    |     5 * (N//2-1) + N//2 -2
        #          N//2 = x           |             x = N//2
        #      4 * (x-1) + x - 2      |         5 * (x-1) + x - 2
        #           4x-6+x            |              5x-5+x-2
        #            5x-6             |               6x-7
        #         5*(N//2)-6          |            6*(N//2)-7

        if N % 2 == 0:
            half = N//2
            # even number of values, so print half on top, rest on bottom

            first = list(map(str,values[:half]))
            if doubly:
                num_spaces = (6*(half))-7
            else:
                num_spaces = (5*(half))-6

            third = list(map(str,values[half:][::-1]))
        
            # aligns top half of list with bottom half, based on # of digits of each item
            for i in range(half):
                diff = len(third[i]) - len(first[i])
                if diff < 0:
                    third[i] = " "*abs(diff) + third[i]
                elif diff > 0:
                    first[i] = " "*diff + first[i]
                num_spaces += len(third[i])-1

            # finally prints results
            print(arrow.join(first))
            print(" "*(len(first[0])-1),"^", " "*(num_spaces-len(first[0])+1), "v", sep="")
            print(back_arrow.join(third))
        
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

    model_ll(chead)


# [x] create reverse_linkedlist function
# [ ] create remove_n_node(start/end) # choose if nth from head or nth from end
# [ ] create insert_node(front/back)